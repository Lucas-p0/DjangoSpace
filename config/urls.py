
from django.contrib import admin;
from django.urls import include, path;
from galeria.views import index;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),

]
