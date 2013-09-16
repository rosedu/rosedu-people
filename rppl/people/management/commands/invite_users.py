import string
import random

from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError

from people.models import Person

EMAIL_TEXT = \
"""Salut %s,

Acesta este contul tău pentru ROSEdu People[1]
Username: %s
Password: %s

Momentan accesul este restricționat numai pentru câțiva utilizatori.
De îndată ce aducem conținut pentru proiecte pe site și rezolvăm
bugurile critice suntem gata să-i dăm drumul pentru întreaga comunitate!

Pentru idei/feedback vă rugăm puneți un issue pe Github[2] sau trimiteți
un mail la people@rosedu.org

Pentru a adăuga proiecte sau ediții folosiți meniul de admin[3]

--Parola este cunoscută doar de tine si este generată automat
  Nu răspunde la acest email, e automat :)

ROSEdu People
Dev Team

[1] http://people.rosedu.org
[2] https://github.com/rosedu/rosedu-people/issues?milestone=3&state=open
[3] http://people.rosedu.org/admin
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

                (last_name, first_name, username, email) = line.split(' ')

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
