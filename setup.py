from setuptools import setup, find_packages

setup(
    name = "django-bootstrap-markdown",
    version = "1.0.4",
    packages = find_packages(),
    author = "A.J. May",
    author_email = "aj7may@gmail.com",
    description = "An extension of the Django Textarea widget made for editing Markdown with a live preview.",
    license = "Creative Commons Attribution-ShareAlike 4.0 International License",
    keywords = "django bootstrap markdown live preview auto scroll",
    url = "http://thegoods.aj7may.com/django-bootstrap-markdown",
    zip_safe = False,
    package_data = {
        'django_bootstrap_markdown': ['static/js/*'],
    },
)