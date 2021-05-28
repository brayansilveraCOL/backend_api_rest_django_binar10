import uuid

from django.db import models
# Utils
from django.contrib.auth.models import AbstractUser

# Models Import
from backend_api.entitys.models import Entity
from backend_api.locations.models import Country


class User(AbstractUser):
    """
    Class User extend  Abstract User
    """
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=False, null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=False, null=False)
    uniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False, unique=True)
    identify = models.CharField('identify user', max_length=255, blank=False, null=False, unique=True)
    image = models.ImageField('Photo', upload_to='profile/', max_length=255, null=True, blank=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
