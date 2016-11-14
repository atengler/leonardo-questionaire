from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class QuestionaireSubmission(models.Model):
    submitted_by = models.ForeignKey(
        getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),
        verbose_name=_("Submitted By"),
        on_delete=models.CASCADE)
    submission = models.ForeignKey(
        'form_designer.FormSubmission',
        verbose_name=_("Form Submission"),
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Questionaire Submission')
        verbose_name_plural = _('Questionaire Submissions')

    def __str__(self):
        return "%s - %s" % (self.submitted_by, str(self.submission.form).encode('utf-8'))

