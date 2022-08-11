from django.contrib import admin
from .models import UserResponse, Question

admin.site.register(Question)
admin.site.register(UserResponse)
