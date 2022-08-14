from django.apps import AppConfig
from django.db.models.signals import post_save  # signal to be used to send email


class CoffeeshopsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "coffeeshops"


class CoffeeshopsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "coffeeshops"

    def ready(self) -> None:
        import coffeeshops.signals
        from coffeeshops.signals import send_new_owner_email
        from coffeeshops.models import CafeOwner
        post_save.connect(send_new_owner_email, sender=CafeOwner)
