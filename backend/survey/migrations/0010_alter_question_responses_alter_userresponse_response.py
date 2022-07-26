# Generated by Django 4.0.6 on 2022-08-02 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_alter_question_responses_alter_userresponse_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='responses',
            field=models.ManyToManyField(to='survey.userresponse'),
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='response',
            field=models.IntegerField(default=0),
        ),
    ]
