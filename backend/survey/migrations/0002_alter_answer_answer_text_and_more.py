# Generated by Django 4.0.6 on 2022-07-26 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(default=''),
        ),
    ]
