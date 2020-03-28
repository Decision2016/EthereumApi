from utils.functions import get_env
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': get_env("POSTGRES_HOST", "ether-db"),
        'PORT': get_env("POSTGRES_PORT", "5433"),
        'NAME': get_env("POSTGRES_DB"),
        'USER': get_env("POSTGRES_USER"),
        'PASSWORD': get_env("POSTGRES_PASSWORD")
    }
}
