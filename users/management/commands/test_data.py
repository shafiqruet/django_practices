from django.core.management.base import BaseCommand
from users.models.user import User
from polls.models import Question, QuestionList, Choice
from users.serializers.users import UserSerializer
import sys
sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())


class Command(BaseCommand):
    def get_family_tree(self, user, count):
        """ return a family tree for a Person object """
        print(user.id)
        children = User.objects.filter(sponsor_id_id=user.id)
        count += 1
        print(f"COunt:{count}")
        if count > 10:
            return

        if not children:
            # this person has no children, recursion ends here
            return {
                'user_id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'sponsor_id': user.sponsor_id_id,
                'children': []}

        # this person has children, get every child's family tree
        return {
            'user_id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'sponsor_id': user.sponsor_id_id,
            'children': [self.get_family_tree(child, count) for child in children],
        }

    def handle(self, **options):
        member = User.objects.get(id=1)

        new_list = self.get_family_tree(member, 1)
        print(new_list)
