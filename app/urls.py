from django.contrib import admin
from django.urls import path, include
from ui import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ui.urls')),
    path('accounts/', include('allauth.urls')),
]
