from django.core.management.base import BaseCommand
from bookstore.models import Book

class Command(BaseCommand):
    help = 'Seed the database with initial books'

    def handle(self, *args, **kwargs):
        books = [
            {
                'title': 'Rich Dad Poor Dad',
                'author': 'Robert Kiyosaki',
                'price': 299.00,
                'description': 'A book about financial education and mindset.',
                'stock': 10
            },
            {
                'title': 'Think and Grow Rich',
                'author': 'Napoleon Hill',
                'price': 350.00,
                'description': 'A classic on personal development and success.',
                'stock': 15
            },
            {
                'title': 'Ikigai',
                'author': 'Héctor García and Francesc Miralles',
                'price': 270.00,
                'description': 'The Japanese secret to a long and happy life.',
                'stock': 8
            }
        ]

        for book_data in books:
            Book.objects.get_or_create(**book_data)

        self.stdout.write(self.style.SUCCESS('✅ Books seeded successfully!'))
