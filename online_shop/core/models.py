from django.db import models

# Create your models here.


class BaseManager(models.Manager):

    def full_archive(self):
        return super().get_queryset()

    def get_queryset(self):
        return super().get_queryset().exclude(is_delete=True)

