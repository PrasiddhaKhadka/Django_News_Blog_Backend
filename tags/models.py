from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
# class Tag(models.Model):
#     label = models.CharField(max_length=255)


# class TaggedItem(models.Model):
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     content_type = models.CharField(max_length=255)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')