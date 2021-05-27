from django.db import models

# import Base Model
from backend_api.utils.baseModel import BaseModel

# import Models
from backend_api.entitys.models import Entity

# Python Libraries
import uuid


# Create your models here.

class Customer(BaseModel):
    """
    Class for Customer
    """
    uniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField('name user', max_length=255, blank=False, null=False)
    lastName = models.CharField('last name user', max_length=255, blank=False, null=False)
    email = models.EmailField('email user')
    identify = models.CharField('identify user', max_length=255, blank=False, null=False, unique=True)
    image = models.ImageField('Photo', upload_to='perfil/', max_length=255, null=True, blank=True)
    password = models.CharField('password user', max_length=300, blank=False, null=False)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.lastName)
