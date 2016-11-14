
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from .widget import *

default_app_config = 'leonardo_questionaire.Config'

LEONARDO_APPS = [
    'leonardo_questionaire'
]

LEONARDO_WIDGETS = [
    QuestionaireWidget,
]

class Config(AppConfig):
    name = 'leonardo_questionaire'
    verbose_name = _('Questionaire')

    def ready(self):
        import .overrides

