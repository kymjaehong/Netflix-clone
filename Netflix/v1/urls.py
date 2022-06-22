from django.urls import path

from .views import HomeView, ProfileList, ProfileCreate, Watch, ShowMovieDetail, ShowMovie


'''
namespace과 함께 사용됩니다.
'''
app_name= 'v1'


'''
1. url= '', views.py 파일에서 HomeViewSet 클래스를 뷰(as_view) 합니다.
'''
urlpatterns= [
    path('', HomeView.as_view(), name= 'home'),
    path('profile/', ProfileList.as_view(), name= 'profile_list'),
    path('profile/create', ProfileCreate.as_view(), name= 'profile_create'),
    path('watch/<str:profile_id>/', Watch.as_view(), name= 'watch'),
    path('movie/detail/<str:movie_id>/', ShowMovieDetail.as_view(), name= 'show_detail'),
    path('movie/play/<str:movie_id>', ShowMovie.as_view(), name= 'play'),

]