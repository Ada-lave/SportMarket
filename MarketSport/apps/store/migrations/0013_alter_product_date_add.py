# Generated by Django 4.1.7 on 2023-06-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_product_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_add',
            field=models.DateField(blank=True, null=True),
        ),
    ]