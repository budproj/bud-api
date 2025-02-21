import uuid6

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid6.uuid7, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
