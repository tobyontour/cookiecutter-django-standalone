test:
	mkdir -p test-tmp
	cd test-tmp && cookiecutter --no-input https://github.com/tobyontour/cookiecutter-django-standalone
	cd test-tmp/django-project-name && make test

clean:
	rm -rf test-tmp