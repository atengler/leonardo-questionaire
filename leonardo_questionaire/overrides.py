# leonardo form designer model override

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import ugettext_lazy as _
from form_designer import models as form_models


def create_form_submission(model_instance, form_instance, request, **kwargs):
    attrs = {
        'form': model_instance,
        'data': json.dumps(form_instance.cleaned_data, cls=DjangoJSONEncoder),
        'path': request.path)
    }

    if 'user' in request and request.user.is_authenticated():
        attrs['submitted_by'] = request.user

    return FormSubmission.objects.create(**attrs)


form_models.create_form_submission = create_form_submission
form_models.FormSubmission.add_to_class(
    'submitted_by', models.ForeignKey(
        'auth.User',
        verbose_name=_("Submited By"),
        related_name='submitters',
        blank=True, null=True))

