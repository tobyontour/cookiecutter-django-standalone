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