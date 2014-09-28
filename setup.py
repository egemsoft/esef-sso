__author__ = 'ahmetdal'

from setuptools import setup

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ''

setup(
    name='esef-sso',
    version='1.0.0.0',
    description='EgemSoft SSO Server and Client code is including.',
    author='EgemSoft',
    author_email='ahmet.dal@egemsoft.net',
    url='https://github.com/egemsoft/esef-sso.git',
    keywords=["django", "egemsoft", "sso", "esefsso"],
    install_requires=[
        "Django",
        "webservices",
        "requests",
        "esef-auth==1.0.0.0",
        "django-simple-sso==0.9.3"
    ],
    dependency_links=[
        "https://github.com/egemsoft/esef-auth/tarball/master/#egg=1.0.0.0",
        "https://github.com/egemsoft/django-simple-sso/tarball/master#egg=0.9.3",
    ],

    packages=[
        'esef_sso_client',
        'esef_sso_client.models',
        'esef_sso_server',
        'esef_sso_server.models',
    ],
    include_package_data=True,
    zip_safe=False,
    license='GPLv3',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ]
)