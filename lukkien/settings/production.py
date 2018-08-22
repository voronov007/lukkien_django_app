import os


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME', 'db_name'),
        'USER': os.getenv('DATABASE_USER', 'db_user'),
        'PASSWORD': os.getenv(
            'DATABASE_PASSWORD', 'db_password'
        ),
        # Or an IP Address that your DB is hosted on
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}
