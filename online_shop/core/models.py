from django.db import models

# Create your models here.


class BaseManager(models.Manager):

    def full_archive(self):
        return super().get_queryset()

    def get_queryset(self):
        return super().get_queryset().exclude(is_delete=True)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = BaseManager()

    is_delete = models.BooleanField(default=False, editable=False, db_index=True)

    def delete(self, using=None, keep_parent=False):
        self.is_delete = True
        self.save(using=using)

    def restore(self):
        self.is_delete = False
        self.save()