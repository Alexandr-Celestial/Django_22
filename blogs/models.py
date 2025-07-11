from django.db import models

# Create your models here.

class Blog(models.Model):
    """Модель продуктов"""
    name = models.CharField(max_length=100, null=False, verbose_name='Имя')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(null=True, upload_to='photos/', verbose_name='Фотография')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    sign_publication = models.BooleanField(default=False, verbose_name='Признак публикации')
    count_view = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'Блоги'
