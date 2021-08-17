from django.urls import path

from accountapp.views import hello_world

app_name='accountapp'
# 127.0.0.1:8000/account/hello_world
#  => accountapp:hello_world 로 만들어주는 함수가 존재

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]