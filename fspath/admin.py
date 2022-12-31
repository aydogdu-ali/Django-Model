from django.contrib import admin
from .models import Student

# Register your models here.

admin.site.register(Student)

# Model kısmında oluşturulan Student tablosunun
# admin panelde görünmesi için Student admin.py
# dosyasına Student modelini import ediyoruz.
