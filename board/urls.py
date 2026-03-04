from django.urls import path
from .views import PostList, PostDetail, PostCreate, add_response

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/response/', add_response, name='add_response'),
]