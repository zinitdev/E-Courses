from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


class CommonModel(models.Model):
    class Meta:
        abstract = True
        ordering = ["-created_date", "active"]

    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Category(CommonModel):
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'


class Course(CommonModel):
    title = models.CharField(max_length=100, unique=True)
    desciption = RichTextField()