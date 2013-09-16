import string
import random

from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError

from people.models import Person

EMAIL_TEXT = \
"""Salut %s,

Acesta este contul tau pentru ROSEdu People[1]
Username: %s
Password: %s

Pentru a schimba parola, poti intra aici[2]

Momentan accesul este restrictionat numai pentru cativa utilizatori.
De indata ce aducem continut pentru proiecte pe site si rezolvam bugurile critice
suntem gata sa-i dam drumul pentru intreaga comunitate!

Pentru idei/feedback poti pune un issue pe Github[3] sau trimite un mail la people@rosedu.org

Pentru a adauga proiecte sau editii folositi meniul de admin[4]

--Parola este cunoscuta doar de tine si este generata automat
  Nu raspunde la acest email, e automat :)

ROSEdu People
Dev Team

[1] http://people.rosedu.org
[2] http://people.rosedu.org/password_change/
[3] https://github.com/rosedu/rosedu-people/issues?milestone=3&state=open
[4] http://people.rosedu.org/admin
"""


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
                if line == '':
                    continue

                (last_name, first_name, email, username) = line.split(' ')

                password_chars = string.ascii_lowercase + string.digits
                password = ''.join(random.choice(password_chars)
                                   for x in range(6))

                person = Person(first_name = first_name,
                                last_name = last_name,
                                username = username,
                                email = email)
                person.set_password(password)
                person.is_staff = True
                person.is_superuser = True

                mail_text = EMAIL_TEXT % (first_name, username, password)

                send_mail('Welcome to ROSEdu People',
                          mail_text,
                          'people@rosedu.org',
                          [email])

		person.save()
                print 'Invited %s %s' % (first_name, last_name)
