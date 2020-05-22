TEST_DIR=test-tmp

test: clean
	mkdir -p $(TEST_DIR)
	cd $(TEST_DIR) && cookiecutter --no-input https://github.com/tobyontour/cookiecutter-django-standalone
	test -f $(TEST_DIR)/django-project-name/django-project-name/tests/templates/_base.html
	cd $(TEST_DIR)/django-project-name && make test

clean:
	rm -rf $(TEST_DIR)