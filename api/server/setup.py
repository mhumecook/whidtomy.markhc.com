# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="What Have I Done to my Home API",
    author_email="mark@markhc.com",
    url="",
    keywords=["Swagger", "What Have I Done to my Home API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    A man&#x27;s (or woman&#x27;s) home is his (or her) castle.  We should all know what&#x27;s going in in our castle.  WHIDTMH allows every man and woman to record what happens in, on or around the castle.  Record your purchases, your renovations, your quotes, your bills, your repair jobs, your warranties ... I mean, you could even record your parties!
    """
)
