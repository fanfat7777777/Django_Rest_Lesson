from django.core.management.base import BaseCommand

from app_authors.models import AuthorModel

class Command(BaseCommand):
    def handle(self, *args, **options):
        AuthorModel.objects.create(first_name='test', last_name='test', birthday_year=1111)