from django import template
from django.conf import settings
from form_designer.models import Form
from leonardo.module.web.models.page import Page
from leonardo_questionaire.models import QuestionaireSubmission

register = template.Library()


@register.assignment_tag()
def submitted(user, form):
    return QuestionaireSubmission.objects.filter(
        submission__form=form,
        submitted_by=user).exists()

@register.assignment_tag()
def get_questionaire(title):
    pages = Page.objects.filter(questionairewidget_set__isnull=False)
    url = None
    for page in pages:
        if page.questionairewidget_set.filter(form__title=title).exists():
            url = page.get_absolute_url()
    return {
        'form': Form.objects.filter(title=title).first(),
        'url': url
    }

@register.assignment_tag()
def get_default_questionaire():
    title = getattr(settings, 'DEFAULT_QUESTIONAIRE_FORM', False)
    if not title:
        return None

    pages = Page.objects.filter(questionairewidget_set__isnull=False)
    url = None
    for page in pages:
        if page.questionairewidget_set.filter(form__title=title).exists():
            url = page.get_absolute_url()
    return {
        'form': Form.objects.filter(title=title).first(),
        'url': url
    }

