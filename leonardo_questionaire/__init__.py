from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_questionaire.Config'


class Default(object):

    config = {
        'DEFAULT_QUESTIONAIRE_FORM': ("", _('Questionaire Form Title'))
    }

    @property
    def apps(self):

        return [
            'leonardo_questionaire'
        ]

    @property
    def widgets(self):
        return [
            'leonardo_questionaire.widget.questionaire.models.QuestionaireWidget'
        ]


class Config(AppConfig):
    name = 'leonardo_questionaire'
    verbose_name = _('Questionaire')

    conf = Default()

default = Default()

