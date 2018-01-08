# -*- coding: utf-8 -*-

import time
import uuid

from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import TheUser


# ----------------------------------------------------------------------------------------------------------------------
@receiver(post_save, sender=User)
def create_additional_data(sender, instance=None, created=False, **kwargs):
    """
    Creates '.models.TheUser' instance and auth_token for this instance after creating User instance.
    """
    if created:
        the_user = TheUser.objects.create(id_user=instance,
                                          auth_token=uuid.uuid5(uuid.NAMESPACE_DNS,
                                                                instance.username + str(instance.date_joined)))
        the_user.save()


# ----------------------------------------------------------------------------------------------------------------------
@receiver(post_delete, sender=TheUser)
def remove_user_obj(sender, instance=None, **kwargs):
    """
    Removes standard django User model if '.models.TheUser' instance was deleted.
    """
    user = instance.id_user
    user.delete()
