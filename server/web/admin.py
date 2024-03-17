from django.contrib.auth.models import Permission, Group
from django.urls import path
from django.shortcuts import render
from .dao import load_amount_courses
from .admin_views import UserAdmin, CourseAdmin, CategoryAdmin, User, Course, Category, admin


class ECourseAdminSite(admin.AdminSite):
    site_header = site_title = "E-Courses Administrator"

    def get_urls(self):
        return [path('statistics/', self.statistics_view, name='statistics')] + super().get_urls()

    def statistics_view(self, request):
        return render(request, 'admin/statistics.html', context={
            'stats': load_amount_courses()
        })


admin_site = ECourseAdminSite(name="E-Course Administrator")

admin_site.register(User, UserAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(Permission)
admin_site.register(Group)