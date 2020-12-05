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
