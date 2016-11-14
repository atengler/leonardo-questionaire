from django import forms
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _
from leonardo_module_forms.widget.form.models import FormWidget


class QuestionaireWidget(FormWidget):
    class Meta:
        abstract = True
        verbose_name = _('Questionaire')
        verbose_name_plural = _('Questionaires')

    def get_template_data(self, request):
        context = {}

        form_class = self.form.form()

        formcontent = request.POST.get(self.prefix + '-_formcontent')

        if request.method == 'POST' and formcontent == smart_text(self.id):
            form_instance = form_class(
                request.POST, request.FILES, prefix=self.prefix)

            if form_instance.is_valid():

                # handle files
                files = self.handle_files(form_instance, request)

                process_result = self.form.process(form_instance, request)

                if 'save_fs' in process_result and request.user.is_authenticated():
                    from leonardo_questionaire.models import QuestionaireSubmission
                    submission = process_result['save_fs']
                    submitted_by = request.user

                    QuestionaireSubmission.objects.create(
                        submission=submission,
                        submitted_by=submitted_by)

                self.process_valid_form(
                    request, form_instance)

                # add reverse reference to files
                for file in files:
                    file.description = process_result[
                        'save_fs'].formatted_data()
                    file.save()

                context['message'] = self.success_message or process_result or u''

            else:
                form_instance = self.get_complete_form(form_instance)
                context["form"] = form_instance

        else:
            form_instance = form_class(prefix=self.prefix)
            form_instance = self.get_complete_form(form_instance)

            context['form'] = form_instance
        # append hidden field for check unique
        if "form" in context:
            context['form'].fields["_formcontent"] = forms.CharField(
                initial=self.id, widget=forms.widgets.HiddenInput)
            context['form'].helper.layout.append("_formcontent")

        return context

