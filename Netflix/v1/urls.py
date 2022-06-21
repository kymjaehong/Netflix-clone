from django.urls import path

from .views import HomeView, ProfileList, ProfileCreate


'''
namespace과 함께 사용됩니다.
'''
app_name= 'v1'


'''
1. url= '', views.py 파일에서 HomeViewSet 클래스를 뷰(as_view) 합니다.
'''
urlpatterns= [
    path('', HomeView.as_view()),
    path('profile/', ProfileList.as_view(), name= 'profile_list'),
    path('profile/create', ProfileCreate.as_view(), name= 'profile_create'),

]