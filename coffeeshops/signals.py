from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from coffeeshops.models import CafeOwner, CoffeeShop


@receiver(post_save, sender=CafeOwner)
def send_new_owner_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Coffee Shop Ownership',
            'You have been selected as the owner of a new coffee shop.',
            'test@coffe.com',
            ['to@example.com'],
            fail_silently=False,
        )
