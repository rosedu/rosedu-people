#!/bin/sh

drop() {
    echo "Droping all tables prefixed with $1_."
    echo
    echo "select name from sqlite_master where type = \"table\";" | ./manage.py dbshell |
    egrep "^$1_" | xargs -I "@@" echo "DROP TABLE @@;" |
    ./manage.py dbshell
    echo "Tables dropped."
    echo
}

cancel() {
    echo "Cancelling Table Drop."
    echo
}

if [ -z "$1" ]; then
    echo "Please specify a table prefix to drop."
else
    echo "Drop all tables with $1_ prefix?"
    select choice in drop cancel;do
        $choice $1
        break
    done
fi
