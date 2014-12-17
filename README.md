# Public Profiles and Activities



Build status: ![Build status](https://travis-ci.org/rosedu/rosedu-people.svg)

## How to test it

```
    pip install -r requirements.txt # installs `django` and `pil` packages
    cd rppl
    mkdir data
    ./manage.py syncdb #select no for superuser
    ./manage.py migrate
	./manage.py loaddata ../initial.json
    ./manage.py runserver localhost:8000
```
    
 - Go to your favorite browser and go to [http://localhost:8000](http://localhost:8000)
   
 - To enter the platform use the people/people login

 - To enter admin console go to [http://localhost:8000/admin](http://localhost:8000/admin)

## How to use South

```
	./manage.py schemamigration people --auto
	./manage.py migrate people
```
