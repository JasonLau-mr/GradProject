# Graduation Project - Student Information System with Data Visualisation

>**Technique**
>Python
>Django
>Sqlite/Mysql

### Static File Setting

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT= os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (     
    os.path.join(BASE_DIR, 'studengapp/static'),               
    )

```

```html
<link rel="stylesheet" type="text/css" href="/static/login.css" />
```

### Field types

>* BooleanField
>* NullBooleanField
>* CharField
>* DateField
>* FloatField
>* IntegerField
>* SmallIntegerField
>* PositiveIntegerField

### Relationship fields


### Manage database using models

>* Create
>* Retrieve
>* Update
>* Delete

