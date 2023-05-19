import psycopg2
import os
import json

from django.conf import settings
from django.db import transaction
import threading

from django.db.models import Sum
from django.db.models import Q
from django.core.management import BaseCommand
from users.models.user import User
from polls.models import Question, QuestionList


class Command(BaseCommand):

    def delete_users(self, users, thread):
        for user in users:
            print(f"First_name:{user.first_name}, Thread: {thread}")

    def handle(self, *args, **options):
        try:
            date_limit = '2022-08-01'
            users = User.objects.filter(created_at__date__gt=date_limit)
            print("Number of User : ", users.count())
            start_from = int(input("Start From \n"))
            upto = int(input("Enter Limit \n"))

            num_of_threads = input(
                "How many processes you would like to run?\n")
            if not num_of_threads:
                print("Thread number must be given")
            else:
                num_of_threads = int(num_of_threads)

            users = users[start_from:upto]
            print(f"Total user found:{users.count()}")
            threads = []
            offset = (upto-start_from)//num_of_threads
            print(f"Offset value:{offset}")

            # declaring shared memory for user count
            total_count = 0
            for x in range(num_of_threads):
                end_to = start_from + offset
                total_count = + end_to
                if x+1 == num_of_threads:
                    end_to = upto
                x = threading.Thread(target=self.delete_users, args=(
                    users[start_from:end_to], x,))
                threads.append(x)
                start_from = end_to

            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

        except Exception as err:
            print(err)

        self.stdout.write(self.style.SUCCESS("It is done."))
