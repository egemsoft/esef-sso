# esef-auth  [![Build Status](https://travis-ci.org/egemsoft/esef-auth.svg)](https://travis-ci.org/egemsoft/esef-auth)

Contains some utilities like data level filtering and its management web interfaces, a manage.py command for fixing all permission, etc.

##Usage

Install it on;
```
pip install git+https://github.com/egemsoft/esef-auth.git
```
and put it in your `INSTALLED_APPS` in your `settings` file.

```
INSTALLED_APPS = (
	    '...',
	    'esef_auth',
	    'guardian',
	    '...'	
	    )
```
Also put `AUTHENTICATION_BACKENDS` in your settings file like;

```
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)
```

## Data Level Filtering
Your model must be extended from abstract `FilteredModel` in `esef-auth`. This will apply a manager to your model. If you don't want to extend the model, you must at least apply that `FilteredModelManager` to your models which you want to make data level filtering on. 

Here is an example of your model definition;

```python
from esef_auth.models.filtered_model import FilteredModel

class MyModel(FilteredModel):
	...		
	related_field=models.ForeignKey('myapp.MyRelatedField')
```

or

```python
from esef_auth.models.manager.filtered_model_manager import FilteredModelManager
from django.db import models

class MyModel(models.Model):
	....
	related_field=models.ForeignKey('myapp.MyRelatedField')
	
	objects=FilteredModelManager()
```

This will provide your model filter method `data-level-filtering`. It won't be applied to all your filter invocation, you will trigger it when ever you want to have it. Before you do this, you should assign `user-object-permission` relation. There is an admin screen which can be used in your project is provided. For filtering, you have to add **change-model_name** permissions

Here is an example to use it;

`MyModel.objects.filter(data_filter_on='')`
`MyModel.objects.filter(data_filter_on='related_field')`
`MyModel.objects.filter(data_filter_on='related_field__second_level_related_field')`

You can do it on the model directly or on its related fields. You can even give more nested level as `data_filter_on` parameter. `esef-auth` will do it on the lookup which you give.

## manage.py Tasks
###fix_permissions:
This will generate all permissions of your models including `proxy models` in your DB. 

It also provides loading permissions from settings file. To load permissions from settings file, you should define them in your settings file like;

```
PERMISSIONS=[
('codename', 'app_label', 'module_name', 'name'),
....
....
]
```

```
python manage.py fix_permissions
```



