# Public Profiles and Activities

Display community activity.

## How to test it

    pip install -r requirements.txt # installs `django` and `pil` packages
    cd rppl
    mkdir data
    ./manage.py syncdb
    ./manage.py loaddata ../initial.json
    ./manage.py runserver localhost:8000


