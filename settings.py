# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password here',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

INSTALLED_APPS = (
    'standalone',
)

SECRET_KEY = 'SECRET KEY for this Django Project'