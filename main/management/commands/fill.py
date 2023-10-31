from django.core.management import BaseCommand
from main.models import Category

class Command(BaseCommand):
    help = 'Заполняет данные в модели Category и очищает старые данные'

    def handle(self, *args, **options):
        # Удаляем все существующие записи в модели Category
        Category.objects.all().delete()

        # Заполняем базу данных новыми данными
        categories_data = [
            {
                'title': 'Фрукты',
                'description': 'Не овощи совсем',
            },
            {
                'title': 'Овощи',
                'description': 'Диванные и не только',
            },

        ]

        for data in categories_data:
            Category.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Данные успешно заполнены'))
