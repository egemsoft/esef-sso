__author__ = 'ahmetdal'

from setuptools import setup

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ''

setup(
    name='esef-sso',
    version='1.0.0.0',
    description='',
    url='https://github.com/egemsoft/esef-sso.git',
    keywords=["django", "egemsoft", "sso", "esefsso"],
    dependency_links=[
        "https://github.com/egemsoft/esef-auth/tarball/master/#egg=esef-auth-1.0.0.0",
        "https://github.com/egemsoft/django-simple-sso/tarball/master#egg=django-simple-sso-0.9.3",
    ],
    install_requires=[
        "Django",
        "webservices",
        "requests",
        "django-simple-sso==0.9.3",
        "esef-auth==1.0.0.0",
    ],
    packages=[
        'esef_sso_client',
        'esef_sso_client.models',
        'esef_sso_server',
        'esef_sso_server.models',
    ],
    include_package_data=True,
    zip_safe=False,
    platforms=['any'],
)