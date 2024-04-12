# Generated by Django 5.0.4 on 2024-04-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_word_word_answera_alter_word_word_answerb_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='word_answerA',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_answerB',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_hmAnswerA',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_hmAnswerb',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_hmRatio',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_otherRatio',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_probaA',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_probaB',
        ),
        migrations.RemoveField(
            model_name='word',
            name='word_slice',
        ),
        migrations.AddField(
            model_name='word',
            name='word_IID',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='word',
            name='word_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='word',
            name='word_code_parent',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='word',
            name='word_gender',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='word',
            name='word_soul',
            field=models.BooleanField(null=True),
        ),
    ]