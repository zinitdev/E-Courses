from web.admin import admin_site
from django.urls import path, include

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('web.urls'))
]