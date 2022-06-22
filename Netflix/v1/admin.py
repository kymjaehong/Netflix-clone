from django.contrib import admin
from .models import CustomUser, Profile, Movie, Video

# Register your models here.
'''
Django 어플리케이션의 Model을 관리하기 위해서 기본적으로 제공하는 관리자 페이지에 Model을 등록할 필요가 있습니다.
'''
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Video)
