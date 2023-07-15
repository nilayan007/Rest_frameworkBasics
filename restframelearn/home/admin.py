from django.contrib import admin
from .models import *
# Register your models here. admins username hp , password : 12345678
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(book)