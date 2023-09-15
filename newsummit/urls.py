from django.contrib import admin
from django.urls import path

from app.views import home, list_all_students

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path("", list_all_students)
]
