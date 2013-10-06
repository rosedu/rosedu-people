## How to run tests

```./manage.py test```

## How to add tests

Anytime you solve a bug or introduce a new feature you need to add a new test
for that.

Currently the tests for the "People" application are found in
rppl/people/tests

The directory structure is this one:

```
rppl
|-- people
|   |-- tests
|   |   |-- __init__.py
|   |   |-- test_forms.py
|   |   |-- test_models.py
|   |   `-- test_views.py
```

Each of the files contains tests for the models views and forms found in the
application.
