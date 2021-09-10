from django.contrib import admin
from django.urls import path
from api.views import StudentAPI

# from api.views import get_students, create_student, update_student, delete_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_students/', StudentAPI.as_view()),
    path('create_student/', StudentAPI.as_view()),
    path('update_student/', StudentAPI.as_view()),
    path('delete_student/', StudentAPI.as_view()),
]
