from django.shortcuts import render
from django.views import View

# 인덱스 페이지나 홈페이지를 가정하고 그것을 처리할 보기
'''
Netflix - Home

'''
class HomeViewSet(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

