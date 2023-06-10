from django.db import models
from io import BytesIO
from PIL import Image
from django.template.defaultfilters import slugify
from django.core.files import File
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
        ('мужской', 'мужской'),
        ('женский', 'женский')
    )

    title = models.CharField(max_length=120, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория', related_name='product')
    slug = models.SlugField()
    descriptions = models.TextField(
        blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    avalible = models.BooleanField(
        default=True, verbose_name='В наличии')
    material = models.CharField(
        max_length=400, verbose_name="Материал", blank=True)
    color = models.CharField(max_length=100, default='None')
    sports_type = models.CharField(
        max_length=40, verbose_name="Вид спорта")
    season = models.CharField(max_length=40, verbose_name="Сезон")
    gender = models.CharField(
        max_length=40, choices=CHOICES_GENDER, verbose_name="Пол", blank=True)
    brand = models.CharField(max_length=120, verbose_name="Брэнд")
    size = models.CharField(max_length=40, verbose_name="Размер")

    date_add = models.DateField()
    date_update = models.DateField(auto_now=True)

    thumbnail = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def newOrOldProduct(self):

        if (dt.datetime.now().date()-self.date_add) < dt.timedelta(days=10):
            print(self.date_add - dt.datetime.now().date())
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        file_name = self.category.title

        
        if self.image1.name:
            print('image ready')
        else:
            self.image1.name = file_name + "/" + self.title + ".png"
            self.image2.name = file_name + "/" + self.title + ".png"
            self.image3.name = file_name + "/" + self.title + ".png"
            self.image4.name = file_name + "/" + self.title + ".png"

        super(Product, self).save(*args, **kwargs)

    def resizeImage(self, image, size=(600, 800)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=95)

        thumb = File(thumb_io, name=image.name)

        return thumb
