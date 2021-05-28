from django.db import models

# import Base Model
from backend_api.utils.baseModel import BaseModel

# Python Libraries
import uuid


# Create your models here.

class TypeEntity(BaseModel):
    """
       Class for TypeEntity
    """
    uniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField('name TypeEntity', max_length=255, blank=False, null=False, unique=True)


class Entity(BaseModel):
    """
    Class for Entity
    """
    uniqueCode = models.UUIDField('Code Unique Generate', default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField('name Entity', max_length=255, blank=False, null=False, unique=True)
    typeEntity = models.ForeignKey(TypeEntity, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name