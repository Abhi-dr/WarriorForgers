# Generated by Django 3.2.8 on 2023-05-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preparations', '0005_auto_20230525_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_quiz',
            name='option1',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='registration_quiz',
            name='option2',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='registration_quiz',
            name='option3',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='registration_quiz',
            name='option4',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='registration_quiz',
            name='question',
            field=models.CharField(max_length=1000),
        ),
    ]