# Generated by Django 4.0.6 on 2022-07-28 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_alter_answer_answer_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer_text',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question',
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='survey.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='survey.survey'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]