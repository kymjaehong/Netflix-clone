from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

'''
(DB에 표시, 사용자에게 표시)
'''
AGE_CHOICES= (
    ('전체관람가', '전체관람가'),
    ('12세 이상 관람가', '12세 이상 관람가'),
    ('15세 이상 관람가', '15세 이상 관람가'),
    ('청소년 관람 불가', '청소년 관람 불가'),

)

'''
(DB에 표시, 사용자에게 표시)
계절 영화,,, 단일 영화,, 등등 추가하기
'''
MOVIE_CHOICES= (
    ('seasonal', 'Seasonal'),
    ('single', 'Single')

)

'''
AbstracUser는 Django의 로그인 기능을 사용하면서, 해당 모델(User)의 컬럼(데이터)들을 수정할 수 있습니다.
'''
class CustomUser(AbstractUser):
    '''
    관계 분야 필드입니다.
    다대다 관계를 저장하는 필드입니다.
    테이블 명: 'Profile'
    blank= True -> 빈 값을 허용합니다.

    null= True를 함께 설정하면 “데이터 없음”에 대해 두 가지 값, 즉 None 과 빈 문자열 을 갖게 됩니다.
    “데이터 없음”에 대해 두 가지 값을 갖는 것은 "None으로 없는 것"과 "빈 문자열로 없는 것"으로 중복됩니다.
    그리고 무엇보다 Null이 아닌 빈 문자열을 사용하는 것이 장고 컨벤션입니다.
    '''
    profiles= models.ManyToManyField('Profile', blank= True)



'''
Model

Django의 모델들은 모두 django.db.models.Model의 subclasses입니다.
각 모델의 속성은 DB 필드입니다.
'''


'''
프로필
    이름: 적은 문자열을 저장하는 문자열 필드, CharField, 최대 길이를 명시해야 합니다.
    나이 제한: 위와 같으며, choices 필드 옵션을 사용하여 드롭 다운 메뉴를 만들었습니다.
    uuid: UUID 전용 필드로 UUID 데이터 유형만 저장할 수 있는 필드, UUIDField
'''
class Profile(models.Model):
    name= models.CharField(max_length= 225)
    age_limit= models.CharField(max_length= 10, choices= AGE_CHOICES)
    uuid= models.UUIDField(default= uuid.uuid4)


'''
영화
    제목: 
    설명: 많은 문자열을 저장하는 필드, TextField, null과 blank 둘 다 True로 설정하는 것을 주의해야 합니다.
    영화 등록일: 날짜 및 시간 데이터를 저장하는 필드, DateTimeField, auto_now_add 메서드를 통해 첫 번째 POST 일시를 등록일로 저장합니다. UPDATE 시, null 값이 되는 것을 주의해야 합니다.
    uuid:
    영화 분류: 

    비디오: 다대다 필드
    flyers: 기타 필드로 이미지 파일을 저장하는 필드, ImageField, upload_to 필드 옵션을 통해 입력 경로에 저장합니다.
    영화 나이 제한:
'''
class Movie(models.Model):
    title= models.CharField(max_length= 225)
    description= models.TextField(blank= True)
    created= models.DateTimeField(auto_now_add= True) 
    uuid= models.UUIDField(default= uuid.uuid4) 
    type= models.CharField(max_length= 10, choices= MOVIE_CHOICES)
# 비디오에 비디오 파일 또는 비디오가 있어야 하는 이름?
# 디비 설명 -> 시작?
    videos= models.ManyToManyField('Video')
    flyer= models.ImageField(upload_to= 'flyers')
    age_limit= models.CharField(max_length= 10, choices= AGE_CHOICES)


# 개별 비디오나 영화 파일을 그대로 유지?
'''
비디오
    제목:
    파일: 
'''
class Video(models.Model):
    # 계절 영화는 제목을 가질 수 있고, 특정 영화는 제목을 가질 수 없다고 에피소드1, 2, 3, 이렇게 갖는다고 가정
    # 단일 영화는 제목이 수행하는 단일 비디오 인스턴스가 이해가 되지 않는다?
    title= models.CharField(max_length= 225, blank= True)
    file= models.FileField(upload_to= 'movies')
    # -> 디비 설정 끝?

# 프로젝트에서 사용할 모델?
#-> views.py
