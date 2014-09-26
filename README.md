# esef-sso

Contains deployable `SSO server` which is run as Django web application and Django client code and utilities.

![egemsoft-logo](http://egemsoft.net/images/logo.png)
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

You need to add your clients as consumer in server from;

```
http://localhost:8000/admin/guardian/userobjectpermission/add/
```
**Note:** The system will generate **SSO\_PUBLIC\_KEY** and **SSO\_PRIVATE\_KEY** and you need to use them on client.

You can also assign permissions to users to prevent them to access a consumer. You need to add `change_consumer` permission to users to allow them to access a consumer.

```
http://localhost:8000/auth/user_object_permission_bulk_create/
```

**Note:** Your internal authorization mechanism should be managed in your application. `esef-sso` will trigger to create a clone of the user in sso-server in your client application. But this user can not login to your application via your login mechanism if it exists. Unuseable password is being set to the user in your application. So you can assign permission on your user management screens to this user.

#esef-sso-client
This is Django client of `esef-sso-server`. This will do all of your SSO stuff with some configuration in your `settings` file.

##Usage
Before you install it, install python and its environments;
Checkout code and install it;

```
pip install git+https://github.com/egemsoft/django-simple-sso.git
pip install git+https://github.com/egemsoft/esef-sso.git
```


If you really want to client set some variables in your settings file;
```
INSTALLED_APPS = (
	 ...,
    'esef_sso_client',
    ...
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'esef_sso_client.backends.ConsumerAccessPermissionBackend',
)

AUTH_USER_MODEL = 'esef_sso_client.EsefSSOUser'

ESEF_SSO_CLIENT_REQUIRED=True
SSO_SERVER = 'http://localhost:8000/server/' #this is the SSO server you'r using
SSO_PUBLIC_KEY = 'DNFGcfYvbvGr4bbndso0YQ3Tkw5oDKsO1NYdnbzR8Ool5soP3AxeFezJ4HtIGs1M'
SSO_PRIVATE_KEY = 'qqbLWf6x01dVBNXtfciG9wwEt7uuwEvflpltF0N2LywNA0JQeSflyuVM8XQqTwWi'

LOGIN_URL = '/sso/login/'
```
**SSO\_PUBLIC\_KEY** and **SSO\_PRIVATE\_KEY** are generate by `esef-sso-server`. You have to set them. 

Let `esef-sso-client` do the rest.
