from django.db import models

# import Base Model
from backend_api.utils.baseModel import BaseModel

# Python Libraries
import uuid


# Create your models here.

class Entity(BaseModel):
    """
    Class for Entity
    """
    uniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField('name user', max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name
