# Generated by Django 3.2.8 on 2023-05-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230518_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='ratings',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
    ]