# Generated by Django 4.0.6 on 2022-08-01 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_remove_answer_survey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
