# Generated by Django 3.2.8 on 2023-05-26 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_video_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mock_test_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='olq_score',
            field=models.FloatField(default=0),
        ),
    ]
