# Generated by Django 5.0.4 on 2024-04-11 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_word_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word_answerA',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_answerB',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_hmAnswerA',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_hmAnswerb',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
