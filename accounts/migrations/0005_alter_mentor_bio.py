# Generated by Django 3.2.8 on 2023-05-24 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230523_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='bio',
            field=models.TextField(blank=True, default='Not Available', max_length=1000),
        ),
    ]