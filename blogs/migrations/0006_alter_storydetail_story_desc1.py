# Generated by Django 3.2.5 on 2021-08-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20210830_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storydetail',
            name='story_desc1',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
