from django.apps import AppConfig


class RestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rest'

    # def ready(self):
    #     calc_shipping_cost.apply_async()