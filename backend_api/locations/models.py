import uuid

from django.db import models

# Utils
from backend_api.utils.baseModel import BaseModel


# Create your models here.

class Country(BaseModel):
    """
    Country Class for Locations
    """
    uniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField('name Country', unique=True, max_length=150)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
