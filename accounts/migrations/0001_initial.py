# Generated by Django 3.2.8 on 2023-05-18 09:11

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='course_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('mobile_number', models.CharField(blank=True, max_length=10)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('courses', models.ManyToManyField(blank=True, to='accounts.Course')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('mobile_number', models.CharField(blank=True, max_length=10)),
                ('registration_score', models.IntegerField(default=0)),
                ('age', models.IntegerField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default=0)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('highschool_score', models.IntegerField(default=0)),
                ('intermediate_score', models.IntegerField(default=0)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('field_type', models.CharField(blank=True, choices=[('Commisioned Officer', 'Commisioned Officer'), ('Non-Commisioned Officer', 'Non-Commisioned Officer')], max_length=100)),
                ('field_of_interest', models.CharField(blank=True, choices=[('NDA', 'NDA'), ('CDS', 'CDS'), ('Territorial Army', 'Territorial Army')], max_length=100)),
                ('courses', models.ManyToManyField(blank=True, to='accounts.Course')),
                ('mentors', models.ManyToManyField(blank=True, to='accounts.Mentor')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='mentor',
            name='students',
            field=models.ManyToManyField(blank=True, to='accounts.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='mentors',
            field=models.ManyToManyField(blank=True, to='accounts.Mentor'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, to='accounts.Student'),
        ),
    ]
