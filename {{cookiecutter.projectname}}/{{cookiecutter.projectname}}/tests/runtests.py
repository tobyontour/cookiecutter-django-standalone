#This file mainly exists to allow python setup.py test to work.
import os
import sys

# Make sure the app is (at least temporarily) on the import path.
APP_DIR = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0, APP_DIR)

def runtests():
    from django.conf import settings
    os.environ['DJANGO_SETTINGS_MODULE'] = '{{ cookiecutter.projectname }}.tests.settings'
    import django
    if hasattr(django, 'setup'):
        django.setup()

    # Now we instantiate a test runner...
    from django.test.utils import get_runner
    TestRunner = get_runner(settings)

    # And then we run tests and return the results.
    test_runner = TestRunner(verbosity=1, interactive=True)
    print('Got here')
    failures = test_runner.run_tests(['{{ cookiecutter.projectname }}.tests'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    runtests(*sys.argv[1:])