# Generated by Django 5.0.4 on 2024-04-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('difficulty', models.IntegerField(blank=True, choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], null=True)),
                ('archive', models.BooleanField(default=False)),
                ('played_counter', models.IntegerField(default=0)),
                ('word_slice', models.CharField(max_length=30)),
                ('word_answerA', models.CharField(max_length=30)),
                ('word_probaA', models.DecimalField(decimal_places=4, max_digits=5)),
                ('word_answerB', models.CharField(max_length=30)),
                ('word_probaB', models.DecimalField(decimal_places=4, max_digits=5)),
                ('word_hmAnswerA', models.CharField(max_length=30)),
                ('word_hmAnswerb', models.CharField(max_length=30)),
                ('word_hmRatio', models.DecimalField(decimal_places=4, max_digits=5)),
                ('word_otherRatio', models.DecimalField(decimal_places=4, max_digits=5)),
                ('tags', models.ManyToManyField(to='core.tag')),
            ],
        ),
    ]
