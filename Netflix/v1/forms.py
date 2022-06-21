from django.forms import ModelForm
from .models import Profile


'''
(예제 학습의 serializers.py 파일 대신 forms.py 파일로 구현)
'''

'''
class Meta
Meta 클래스는 권한, 데이터베이스 이름, 단 복수 이름, 추상화, 순서 지정 등과 같은 모델에 대한 다양한 사항을 정의하는 데 사용할 수 있습니다. (선택 사항)

ordering= ['필드 명'], 오름차순
        = ['-필드 명'] 내림차순
fields= ['필드 명', ...], default는 전체이지만 특정 필드 명만 보고 싶을 때 설정합니다.
exclude= ['필드 명', ...] 전체 필드 중 보고 싶지 않은 필드 명을 설정합니다.

위 두 방법 중 하나를 선택해서 사용하면 될 것 같습니다.
'''
class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        exclude= ['uuid']