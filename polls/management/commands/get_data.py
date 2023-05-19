from django.core.management.base import BaseCommand

from polls.models import Question


class Command(BaseCommand):

    def data_check():
        print("Working here")
        # i will write code here
        print("Data here")

    def handle(self, **options):
        result = Question.objects.all()
        for row in result:
            print(row.id)

        print("Script run done")
