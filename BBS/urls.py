
from django.urls import path, include
from BBS import views

app_name = 'bbs'

urlpatterns = [
    path('', views.post_list, name='글 리스트'),
    path('write/', views.post_form, name='글작성'),
    path('writing/', views.post_write, name='writing'),
    path('<int:p_num>/', views.post_detail, name='글내용'),
    path('<int:p_num>/like', views.post_like, name='like'),
    path('<int:p_num>/add_c', views.comment_write, name='comment_write'),
]
