# Generated by Django 3.1.4 on 2020-12-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_url',
            field=models.CharField(default='https://anirudhjwala.me', max_length=255),
        ),
    ]
