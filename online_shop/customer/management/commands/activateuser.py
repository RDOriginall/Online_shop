from argparse import ArgumentParser
from django.core.management import BaseCommand, CommandError
from core.models import User

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-p', '--phone', required=True, help='Enter your phone please!')

    def handle(self, *args, **optinos):
        phone = optinos['phone']
        try:
            user = User.objects.get(phone=phone)
            user.is_active = True
            user.save()
            print(self.style.SUCCESS('Your phone number activated successfully!'))
        except:
            print(self.style.ERROR('This phone number does not exist!'))
