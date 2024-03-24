from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.contrib import admin
from django.utils.html import mark_safe

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    @admin.display(description="Avatar")
    def avatar_preview(self):
        return mark_safe(
        '<img src="{}" width="60" height="60" />'.format(self.avatar.url)
    )


class CommonModel(models.Model):
    class Meta:
        abstract = True
        ordering = ["created_date", "active"]

    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Category(CommonModel):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Course(CommonModel):
    title = models.CharField(max_length=100, unique=True)
    desciption = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Lesson(CommonModel):
    name = models.CharField(max_length=80)
    