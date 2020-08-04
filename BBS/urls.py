
from django.urls import path, include
from BBS import views

urlpatterns = [
    path('', views.post_list, name='글 리스트'),
    path('<int:p_num>', views.post_detail, name='글내용'),
]
