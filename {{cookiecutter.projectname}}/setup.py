import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{{cookiecutter.projectname}}-pkg-{{cookiecutter.pypiusername}}", # Replace with your own username
    version="0.0.1",
    author="{{ cookiecutter.author}}",
    author_email="{{ cookiecutter.author_email}}",
    description="A django article app",
    long_description=long_description,
    long_description_content_type="text/restructured_text",
    url="{{cookiecutter.project_url}}",
    packages=setuptools.find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires='>=3.6',
    install_requires=[
        'Django>=3.0.0'
    ],
    test_suite='{{cookiecutter.projectname}}.tests.runtests.runtests'
)