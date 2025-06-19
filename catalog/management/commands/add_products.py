from django.core.management import BaseCommand, call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Добавляет данные из фикстуры в БД'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()
        call_command('loaddata', 'fixture_catalog.json')
        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены'))