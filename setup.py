#!/usr/bin/env python

import os
from setuptools import setup, find_packages


readme = open('README.rst').read()

setup(
    name="django-bootstrap-markdown",
    version="1.5.3",
    packages=find_packages(),
    author="A.J. May",
    author_email="aj7may@gmail.com",
    maintainer="A.J. May",
    maintainer_email="aj7may@gmail.com",
    description="""An extension of the Django Textarea widget made for
    editing Markdown with a live preview.""",
    long_description=readme,
    license="MIT License",
    keywords="django bootstrap markdown live preview auto scroll",
    url="http://thegoods.aj7may.com/django-bootstrap-markdown",
    zip_safe=False,
    package_data={
        'django_bootstrap_markdown': [
            'static/js/*',
            'static/css/*',
            'templates/django_bootstrap_markdown/*'
        ],
    },
    install_requires=[
        'Pillow>=2.2.2',
        'django-imagekit>=3.1'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
