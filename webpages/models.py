from django.db import models


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    button_text = models.CharField(max_length=255)
    button_url = models.CharField(
        max_length=255, default='https://anirudhjwala.me')

    photo = models.ImageField(upload_to='media/slider/%Y/')

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    role = models.CharField(max_length=255)

    facebook_link = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=255)

    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
