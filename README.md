# Pipenv

Install from Pipfile, if there is one:
```
$ pipenv install
```

Or, add a package to your new project:
```
$ pipenv install <package>
```

This will create a Pipfile if one doesn’t exist. If one does exist, it will automatically be edited with the new package you provided.

Next, activate the Pipenv shell:
```
$ pipenv shell
$ python --version
```

To deactivate the pipenv:
```
deactivate
```

# Pytest

To run the tests:
```
pipenv run pytest
```

To display the output then add the following options:
```
pipenv run pytest -rx
```

To run marked test use:
```
pytest -m <markername> -v
```
where <markername> can be, for this repository:
```
pipenv run pytest -m great
```

- Pipenv install <package> vs pip install <package>

If you are installing using a pipenv environment you should always install your packages using pipenv, this way it will update your pipfile.lock file. Also be careful because pip install <package> will pretty much work anywhere, it's not installing packages to your virtual environment, it's installing them into your computer. Pipenv will update your Pipfile.lock and actually install into your pipenv virtual enviroment if you have one open.

It's rarely a good idea to pip install <package> outside of a virtualenv.



# Unittest
```
pipenv run python tests/assertion/test_unittest_special_assertions.py
```

```
pipenv run python -m unittest discover
```

If the above command is not finding any tests is becuase you didn't create a __init__.py for every folder: https://stackoverflow.com/questions/5088960/python-m-unittest-discover-does-not-discover-tests

# References

- Intro to pytest:
https://github.com/pluralsight/intro-to-pytest

- pytest: How to mock in Python
https://changhsinlee.com/pytest-mock/

- Pytest with Marking, Mocking, and Fixtures in 10 Minutes
https://towardsdatascience.com/pytest-with-marking-mocking-and-fixtures-in-10-minutes-678d7ccd2f70

- Basic Usage of Pipenv:
https://pipenv-fork.readthedocs.io/en/latest/basics.html

- How to create a modern pytest dev environment with vscode:
https://blog.thenets.org/how-to-create-a-modern-pytest-dev-environment-with-vscode/

- Pytest mock:
https://changhsinlee.com/pytest-mock/

- Library for decorator dataclasses:
https://docs.python.org/3/library/dataclasses.html
https://realpython.com/python-data-classes/
