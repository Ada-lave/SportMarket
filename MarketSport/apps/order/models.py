from django.db import models
from apps.store.models import Product

class Order(models.Model):
    name = models.CharField(max_length=120, verbose_name="Имя и Фамилия")
    email = models.CharField(max_length=120, verbose_name="Почта")
    address = models.CharField(max_length=120, verbose_name="Адрес")
    mobile = models.CharField(max_length=50)

    createAt = models.DateTimeField(auto_now_add=True, verbose_name='Время создания ')

    paid = models.BooleanField(default=False, verbose_name="Оплата")
    paid_amount = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} заказ {self.id}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order.name} {self.id}"
