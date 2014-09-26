# esef-sso

Contains deployable `SSO server` which is run as Django web application and Django client code and utilities.


#esef-sso-server
This is Django web application to provide SSO server. It contains, login, logout, asking user is athenticated and consumer authorization. This means, this is not an embeded library that you may want to put in `INSTALLED_APPS` of your project settings. This is required to be deploy somewhere if you want to use `esef-sso-client`. 
##Usage
Before you install it, install python and its environments;
Checkout code and install it;

```
git clone git@github.com:egemsoft/esef-sso.git
cd esef-sso
pip install -r requirements.txt
```

Deploy it as simple
```
python manage.py runserver
```
or deploy it on gunicorn behind a reverse proxy like nginx.

The server uses `sqllite3` database as default. If you want to change it, you can give it in `settings.py` here;

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```


#esef-sso-client
This is Django client of `esef-sso-server`. This will do all of your SSO stuff with some configuration in your `settings` file.

##Usage
Before you install it, install python and its environments;
Checkout code and install it;

```
git clone git@github.com:egemsoft/esef-sso.git
cd esef-sso
pip install -r requirements.txt
```

Deploy it as simple
```
python manage.py runserver
```
or deploy it on gunicorn behind a reverse proxy like nginx.

The server uses `sqllite3` database as default. If you want to change it, you can give it in `settings.py` here;

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
