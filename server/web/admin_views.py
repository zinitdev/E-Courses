from django.contrib import admin
from .forms import CourseAdminForm
from .models import User, Category, Course


class CourseInline(admin.StackedInline):
    model = Course


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ["id", "title", "desciption", "category"]
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = [CourseInline]
    prepopulated_fields = {"slug": ("name",)}


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "avatar_preview"]