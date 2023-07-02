from django.apps import AppConfig


# The RpdsAppConfig class is a Django app configuration class with a default auto field and the name
# 'rpds_app'.
class RpdsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rpds_app'
