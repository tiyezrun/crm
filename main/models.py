from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    ROLE = [
        (1, 'admin'),
        (2, 'cashier'),
        (3, 'manager'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveIntegerField(choices=ROLE, default=2, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwrgs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
