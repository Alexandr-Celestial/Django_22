from django.core.management import BaseCommand, call_command

from users.models import CustomUser


class Command(BaseCommand):
    help = 'Создаёт суперпользователя'

    def handle(self, *args, **kwargs):
        super_user: CustomUser = CustomUser.objects.create(email='admin@gmail.com', is_staff=True, is_active=True, is_superuser=True)
        super_user.set_password('12345')
        super_user.save()
        self.stdout.write(self.style.SUCCESS('Суперпользователь успешно добавлен'))