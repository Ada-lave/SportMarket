# Generated by Django 4.1.7 on 2023-06-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_date_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default=1, max_length=120, verbose_name='Брэнд'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], max_length=40, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, max_length=400, verbose_name='Материал'),
        ),
        migrations.AddField(
            model_name='product',
            name='season',
            field=models.CharField(default=1, max_length=40, verbose_name='Сезон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default=1, max_length=40, verbose_name='Размер'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sports_type',
            field=models.CharField(default=1, max_length=40, verbose_name='Вид спорта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_add',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='descriptions',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
