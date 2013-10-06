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

If you need to create an instance of some model use factory instdead of
Model.objects.create().
You can find factories in:

```
rppl
|-- people
|   |-- factories
|   |   |-- {model_name}_factory.py
```

## Tests for Bugs

The flow for solving a bug is:
- create a [regression test](http://en.wikipedia.org/wiki/Regression_testing)
  to reproduce the bug - if it's possible (90% is possible)
- fix the bug and see that the regression test passes

Add the bug's issue number in the test's docstring.

