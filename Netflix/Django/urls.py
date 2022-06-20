"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

'''
0. admin 페이지
1. url= '', include({앱 명}.{url 파일 명}), namespcae는 app_name과 함께 사용해야 하며 app_name은 {앱 명}/urls.py 파일 안에 작성합니다.


'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('v1.urls', namespace= 'v1')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
