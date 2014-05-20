#!/usr/bin/env python

import os
from setuptools import setup, find_packages

try:
    from pypandoc import convert

    def read_md(f):
        try:
            d = convert(f, 'rst')
        except OSError:
            print("warning: You do not have pandoc installed, could not convert README.") 
            d = open(f, 'r').read()
        return d
except ImportError:
    print("warning: pypandoc module not found, could not convert README.")
    read_md = lambda f: open(f, 'r').read()

setup(
    name="django-bootstrap-markdown",
    version="1.6.0",
    packages=find_packages(),
    author="A.J. May",
    author_email="aj7may@gmail.com",
    maintainer="A.J. May",
    maintainer_email="aj7may@gmail.com",
    description="""An extension of the Django Textarea widget made for
    editing Markdown with a live preview.""",
    long_description=read_md('README.md'),
    license="MIT License",
    keywords="django bootstrap markdown live preview auto scroll",
    url="http://thegoods.aj7may.com/django-bootstrap-markdown",
    zip_safe=False,
    include_package_data=True,
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
