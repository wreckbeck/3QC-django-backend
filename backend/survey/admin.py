from django.contrib import admin
from .models import Survey, UserResponse, Question

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(UserResponse)
