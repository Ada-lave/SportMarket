from django.db import models
from apps.store.models import Product

class Order(models.Model):
    name = models.CharField(max_length=120, verbose_name="Имя и Фамилия")
    email = models.CharField(max_length=120, verbose_name="Почта")
    address = models.CharField(max_length=120, verbose_name="Адрес")
    mobile = models.CharField(max_length=50, verbose_name="Мобильный")

    createAt = models.DateTimeField(auto_now_add=True ,verbose_name='Время создания ')

    paid = models.BooleanField(default=False, verbose_name="Оплата")
    paid_amount = models.FloatField(blank=True, null=True, verbose_name="Сумма к оплате")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.name} заказ {self.id}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    price = models.FloatField(verbose_name="Цена")
    quantity = models.IntegerField(verbose_name="Количество")


    class Meta:
        verbose_name = 'Содержимое заказа'
        verbose_name_plural = 'Содержимое заказа'

    def __str__(self):
        return f"{self.order.name} {self.product.title} {self.id}"
