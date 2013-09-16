import string
import random

from django.core.management.base import BaseCommand, CommandError

from people.models import Person

class Command(BaseCommand):
    help = 'Invite users to join People from a file'

    def usage(self, command_name):
        return ('%s file\n'
                '\tfile is a text document with the following format\n'
                '\tlast_name first_name username email') % command_name

    def handle(self, *options, **kwoptions):
        if len(options) != 1:
            raise CommandError('Must provide a file')

        with open(options[0]) as f:
            for line in f:
                line = line.strip()
                # ingore blank lines
                print line
                if line == '':
                    continue

                (last_name, first_name, username, email) = line.split(' ')

                password_chars = string.ascii_lowercase + string.digits
                password = ''.join(random.choice(password_chars)
                                   for x in range(6))

                print first_name, last_name, username
                person = Person(first_name = first_name,
                                last_name = last_name,
                                username = username,
                                email = email)
                person.set_password(password)
                person.is_staff = True
