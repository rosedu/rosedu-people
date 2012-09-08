#!/usr/bin/env python
#
# Import people from the csv spreadhseet available on Google Apps

import sys
import csv

from django.core.management import setup_environ

def init():
    import settings
    setup_environ(settings)

def import_from_csv(csv_reader):
    from rppl.people.models import Person

    for row in csv_reader:
        p = Person(first_name=row[2],
                   last_name=row[1],
                   username=row[9])
        try:
            p.save()
            print "Added %s %s." % (row[2], row[1])
        except:
            print "%s %s exists!" % (row[2], row[1])

def main():
    if len(sys.argv) != 2:

        print "Usage: import_members_from_csv.py <file>"
        sys.exit(2)

    try:
        init()
    except:
        #Gotta catch 'em all!
        print "No settings.py file."
        sys.exit(1)

    import_from_csv(csv.reader(open(sys.argv[1], "rb"), delimiter=',',
                    quotechar='|', quoting=csv.QUOTE_MINIMAL))
    print "Done"

if __name__ == "__main__":
    main()

