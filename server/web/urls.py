from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r"^__debug__/", include("debug_toolbar.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
