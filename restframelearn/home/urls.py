from django.contrib import admin
from django.urls import path  , include
from .views import *
urlpatterns = [
    # path('',home),
    # path('student/',poststudent),
    # path('updateStudent/<id>/',update_student),
    # path('deleteStudent/<id>/',delete_student),
    path('getbook/',get_book),
    #path('student/',StudentAPI.as_view()),
    path('student-list/',StudentList.as_view()),
    path('Studentdeleteupdate/<id>/',Studentdeleteupdate.as_view())
]