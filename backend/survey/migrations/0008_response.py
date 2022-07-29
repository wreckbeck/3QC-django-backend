# Generated by Django 4.0.6 on 2022-07-29 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_remove_answer_question_question_answers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.ManyToManyField(to='survey.question')),
                ('selected_answers', models.ManyToManyField(to='survey.answer')),
                ('survey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='survey.survey')),
            ],
        ),
    ]
