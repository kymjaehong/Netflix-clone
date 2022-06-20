from django.urls import path
from .views import HomeViewSet

'''
namespace과 함께 사용됩니다.
'''
app_name= 'v1'

'''
1. url= '', views.py 파일에서 HomeViewSet 클래스를 뷰(as_view) 합니다.
'''
urlpatterns= [
    path('', HomeViewSet.as_view())

]