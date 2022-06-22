from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from v1.models import Profile, Movie

from .forms import ProfileForm


'''
render, redirect
render: 불러오고 싶은 template_name 즉, html 파일을 띄웁니다.
redirect: urls.py 파일에서 paht에 설정한 name 즉, url로 이동합니다.
'''


'''
Netflix - Home
'''
class HomeView(View):
    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            #print('1',redirect('v1:profile_list'))-> <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/profile/">
            #                                      -> 로그인이 된 상태라면, /profile/ url로 이동 == 리디렉션(302)
            return redirect('v1:profile_list')

        return render(request, 'index.html')


'''
Django에서 request.user를 통해 request의 유저를 알 수 있습니다.
Django에서 지원하는 session 방식의 로그인 / rest_framework에서 지원하는 JWT 등 로그인을 하면 request.user의 정보를 가져올 수 있습니다.

Django는 자동으로 생성된 DB 접근 API를 제공하며, 이를 Django QuerySet이라고 합니다.
<QuerySet [<클래스 명: 테이블 명 object (n)>]>
(테이블 명은 클래스 명과 동일합니다.)

페이지 권한 설정
Decorator 접근에는 로그인이 요구됩니다. 
클래스 뷰에서 URL에 접근했을 클래스 뷰를 호출할 때, dispatch가 호출(실행)됩니다.

decorator를 지정할려면 원래 dispatch 함수를 만들어서 decorator를 지정해야 하지만, Django의 method_decorator를 사용하면 바로 dispatch 지정이 가능합니다.
'''


'''
Netflix - ProfileList
'''
@method_decorator(login_required, name= 'dispatch')
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        # print('1',request.user)-> test-> 로그인 email: test@naver.com 
        # print('2',request.user.profiles)-> v1.Profile.None-> {앱 명}.{테이블 명}.None?
        # print('3',request.user.profiles.all())->  <QuerySet [<Profile: Profile object (3)>, <Profile: Profile object (4)>]>
        #                                           <QuerySet [<Profile: Profile object (5)>]>
        # print('4', request.user.objects)-> .all()까지도 에러 발생
        profiles= request.user.profiles.all()

        # print(render(request, 'profileList.html', {
        #     'profiles': profiles 
        # }))-> <HttpResponse status_code=200, "text/html; charset=utf-8">
        return render(request, 'profileList.html', {
            'profiles': profiles 
        })


'''
Netflix - ProfileCreate
- get()

- post()
프로필 객체 생성

'''
@method_decorator(login_required, name= 'dispatch')
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        # form for creating profile
        form= ProfileForm()
        # print(form)->
        # <tr>
        #     <th><label for="id_name">Name:</label></th>
        #     <td>

        #     <input type="text" name="name" maxlength="225" required id="id_name">


        #     </td>
        # </tr>

        # <tr>
        #     <th><label for="id_age_limit">Age limit:</label></th>
        #     <td>

        #         <select name="age_limit" required id="id_age_limit">
        #     <option value="" selected>---------</option>

        #     <option value="전체관람가">전체관람가</option>

        #     <option value="12세 이상 관람가">12세 이상 관람가</option>

        #     <option value="15세 이상 관람가">15세 이상 관람가</option>

        #     <option value="청소년 관람 불가">청소년 관람 불가</option>

        # </select>




        #     </td>
        # </tr>

        return render(request, 'profileCreate.html', {
            'form': form
        }) 

    def post(self, request, *args, **kwargs):
        form= ProfileForm(request.POST or None)
        # print(form)-> get()에서 차이점
        # <input type="text" name="name" value="과연" maxlength="225" required id="id_name">
        # <option value="청소년 관람 불가" selected>청소년 관람 불가</option>

        # print(form.is_valid())-> form에 데이터가 있으면 True 반환
        if form.is_valid():
            # print(form.cleaned_data)
            # Output: {'name': '멋장이', 'age_limit': '청소년 관람 불가'}
            '''
            profile 변수에 Profile 클래스에서 생성한 데이터를 저장합니다.
            profiles에 새롭게 생성한 profile 변수를 추가합니다.
            마지막으로, profile_list(ProfileList.html)로 리디렉션을 합니다.
            '''

            '''
            object 생성
            .objects.create()
            '''
            # print(form.cleaned_data)-> {'name': '테스트3', 'age_limit': '전체관람가'}
            # print(**form.cleaned_data)-> 에러 발생
            profile= Profile.objects.create(**form.cleaned_data)
            # print(profile)-> Profile object (9)

            if profile:
                '''
                ManyToManyField, 필드 업데이트를 하려면 .add()를 사용해야 합니다.
                '''
                request.user.profiles.add(profile)
                return redirect('v1:profile_list')

        return render(request, 'profileCreate.html', {
            'form': form
        })


'''
Netflix - Movie List
'''
@method_decorator(login_required, name= 'dispatch')
class Watch(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            profile= Profile.objects.get(uuid= profile_id)
            # db에서 모든 영화 수집
            '''
            .filter()와 .all()은 QuerySet을 반환합니다.
            '''
            movies= Movie.objects.filter(age_limit= profile.age_limit)

            # 프로필의 해당 페이지 목록에 접속하고 있는지 확인
            if profile not in request.user.profiles.all():
                return redirect('v1:profile_list')
            
            return render(request, 'movieList.html', {
              'movies': movies  
            })
        # 프로필 테이블이 존재하지 않으면, 프로필 리스트 url로 이동
        except Profile.DoesNotExist:
            return redirect('v1:profile_list')


'''
Netflix - Movie Detail
'''
@method_decorator(login_required, name= 'dispatch')
class ShowMovieDetail(View):
    def get(self, request, movie_id, *args, **kwarg):
        try:
            movie= Movie.objects.get(uuid= movie_id)
            # print(movie)-> 200 3686

            return render(request, 'movieDetail.html', {
                'movie': movie
            })
        
        except Movie.DoesNotExist:
            return redirect('v1:profile_list')



@method_decorator(login_required, name= 'dispatch')
class ShowMovie(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie= Movie.objects.get(uuid= movie_id)
            '''
            .values()
            QuerySet을 딕셔너리 형태로 반환합니다.
            '''
            movie= movie.videos.values()
            # print(movie)-> <QuerySet [{'id': 1, 'title': '', 'file': 'movies/baby.mp4'}]>
            # print(list(movie))-> [{'id': 1, 'title': '', 'file': 'movies/baby.mp4'}]

            return render(request, 'showMovie.html', {
                'movie': list(movie)
            })

        except Movie.DoesNotExist:
            return redirect('v1:profile_list')