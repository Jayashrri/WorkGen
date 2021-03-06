# Generated by Django 2.1 on 2018-08-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='question_type',
            field=models.IntegerField(choices=[(1, 'TEXT'), (2, 'FILL IN THE BLANKS'), (3, 'MCQ')], null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_weightage',
            field=models.IntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], null=True),
        ),
    ]
