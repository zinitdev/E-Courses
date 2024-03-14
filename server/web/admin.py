from django.contrib.auth.models import Permission
from django.contrib import admin
from .form import CourseAdminForm
from .models import User, Category, Course

class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Permission)
admin.site.site_header = admin.site.site_title = "E-Courses Administrator"