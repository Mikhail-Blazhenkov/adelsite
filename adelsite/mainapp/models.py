from django.db import models

# Create your models here.
class PortfolioItem(models.Model):
    name = models.CharField(max_length=100)  # Имя человека
    photos = models.ImageField(upload_to='media/')  # Поле для загрузки фотографий