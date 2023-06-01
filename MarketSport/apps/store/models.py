from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
import datetime as dt
import os


class Category(models.Model):
    title = models.CharField(max_length=60, unique=True, db_index=True)
    slug = models.SlugField(unique=True, db_index=True, blank=True)
    

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.title



class Product(models.Model):
    CHOICES_GENDER = (
        ('m', 'мужской'),
        ('f', 'женский')
    )

    title = models.CharField(max_length=120, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    slug = models.SlugField()
    descriptions = models.TextField(blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(blank=True)
    avalible = models.BooleanField(default=True, verbose_name='В наличии')
    material = models.CharField(max_length=400, verbose_name="Материал", blank=True)
    sports_type = models.CharField(max_length=40, verbose_name="Вид спорта")
    season = models.CharField(max_length=40, verbose_name="Сезон")
    gender = models.CharField(max_length=40, choices=CHOICES_GENDER, verbose_name="Пол", blank=True)
    brand = models.CharField(max_length=120, verbose_name="Брэнд")
    size = models.CharField(max_length=40, verbose_name="Размер")

    date_add = models.DateField()
    date_update = models.DateField(auto_now=True)

    

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары' 
    
    def __str__(self):
        return self.title

    def newOrOldProduct(self):
        
        if (dt.datetime.now().date()-self.date_add)<dt.timedelta(days=10):
            print(self.date_add - dt.datetime.now().date())
            return True
        else:
            return False


    def save(self, *args, **kwargs):
        file_name = self.category.title
        
        self.image.name = file_name + "/" + self.title + ".png"
        
        super(Product, self).save(*args, **kwargs)

        
