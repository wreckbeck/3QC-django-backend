# Generated by Django 4.0.6 on 2022-07-29 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_answer_survey_alter_answer_question_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='survey',
        ),
    ]
