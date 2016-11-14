# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('form_designer', '0002_auto_20160826_1544'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionaireSubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submission', models.ForeignKey(verbose_name='Form Submission', to='form_designer.FormSubmission')),
                ('submitted_by', models.ForeignKey(verbose_name='Submitted By', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Questionaire Submission',
                'verbose_name_plural': 'Questionaire Submissions',
            },
        ),
    ]
