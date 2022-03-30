# from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Our custom user is used so we can add any user attributes for
    methods on top of the AbstractUser in the future.
    """
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
