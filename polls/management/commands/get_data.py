from django.core.management.base import BaseCommand

from polls.models import Question


class Command(BaseCommand):
    def handle(self, **options):
        result = Question.objects.all()
        for row in result:
            print(row.id)
