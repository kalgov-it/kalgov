# Generated by Django 4.1 on 2022-09-10 11:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_description_postjob_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='postjob',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
