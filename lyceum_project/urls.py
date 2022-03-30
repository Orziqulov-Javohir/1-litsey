
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Natijalar"
admin.site.index_title = "Natijalar"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('probalar_app.urls'))
]
