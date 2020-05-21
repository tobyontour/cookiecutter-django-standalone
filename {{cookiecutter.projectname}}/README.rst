=================
{{cookiecutter.project_title}}
=================

{{cookiecutter.project_title}} is a Django app...

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "{{cookiecutter.projectname}}" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        '{{cookiecutter.projectname}}',
    ]

2. Include the articles URLconf in your project urls.py like this::

    path('example/', include('{{cookiecutter.projectname}}.urls')),

3. Run ``python manage.py migrate`` to create the models.

Development
-----------

1. Make sure you have python3 installed.
2. Run the tests::

    make test

3. Check your local environment is up to date::

    make upgrade-local

4. Build the package::

    make build

5. Upload it (assumes you have setup the API key)::

    make upload

See `Packaging Projects <https://packaging.python.org/tutorials/packaging-projects/>`_