# Django Standalone App Cookiecutter

Includes:

* Testing and coverage.
* Makefile for installation and tests.

## Usage

Install [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html)

Run:

    cookiecutter https://github.com/tobyontour/cookiecutter-django

Enter the data required at the prompts.

Run the tests to see that it all passes:

    make test

Check your coverage:

    make coverage

It's easy to copy your own app into the directory structure but just be aware
that `tests/runtests.py` and `tests/urls.py` shouldn't be overridden (as they
were what caused me the pain that made me make this).

Check the `setup.py` file has all the correct values in it (such as dependencies)
before uploading to pypi.

See [Packaging Projects](https://packaging.python.org/tutorials/packaging-projects/)
for how to create API keys and all that shenanigans and the README.rst file in the
directory.

## To Do

More docs!

## License

Just to be clear, the LICENSE file in this repo only applies to the cookiecutter. What
you build with it is yours.

## Development

1. Checkout the repo.
2. Make sure you have these installed:
    * Cookiecutter
    * python3
3. Run the tests to make sure it's working:

    make test

## References

Getting the testing system setup and running smoothly was the toughest part. You can
create a whole Django environment or you can bootstrap just part of it. The latter seems
like a better bet and what I've gone with.

* https://packaging.python.org/tutorials/packaging-projects/
* https://setuptools.readthedocs.io/en/latest/setuptools.html#test-build-package-and-run-a-unittest-suite
* https://python-packaging.readthedocs.io/en/latest/testing.html
* http://django-standalone-apps.com/part1/testing.html
* https://docs.djangoproject.com/en/3.0/topics/testing/advanced/
* https://docs.djangoproject.com/en/3.0/intro/reusable-apps/
* https://www.ericholscher.com/blog/2009/jun/29/enable-setuppy-test-your-django-apps/
* https://github.com/bzzzzzz/django-yandex-cash-register/blob/master/yandex_cash_register/tests/runtests.py
* https://cookiecutter.readthedocs.io/en/latest/README.html