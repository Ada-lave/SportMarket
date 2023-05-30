from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
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
    title = models.CharField(max_length=120, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    slug = models.SlugField()
    descriptions = models.TextField(blank=True)
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(blank=True)
    avalible = models.BooleanField(default=True, verbose_name='В наличии')
    date_add = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    date_update = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары' 
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        file_name = self.category.title
        
        self.image.name = file_name + "/" + self.title + ".png"
        
        super(Product, self).save(*args, **kwargs)

        
