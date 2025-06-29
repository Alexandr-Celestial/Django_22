from django.db import models

# Create your models here.


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField(max_length=100, null=False, verbose_name='Имя')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')



    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):
    """Модель продуктов"""
    name = models.CharField(max_length=100, null=False, verbose_name='Имя')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(null=True, upload_to='photos/', verbose_name='Фотография')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.PositiveIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'





