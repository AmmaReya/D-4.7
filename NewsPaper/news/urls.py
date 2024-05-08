from django.urls import path
<<<<<<< HEAD
from .views import (PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, subscriptions)


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),

    path('news/create/', PostCreate.as_view(), name='new_create'),
    path('news/<int:pk>/update/', PostUpdate.as_view(), name='new_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='new_delete'),

    path('articles/create/', PostCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/update/', PostUpdate.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),

    path('subscriptions/', subscriptions, name='subscriptions')
=======
from . import views


urlpatterns = [
   path('', views.PostList.as_view(), name='post_list'),
   path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
   path('search/', views.PostSearch.as_view(), name='post_search'),

   path('news/create/', views.PostCreate.as_view(), name='new_create'),
   path('news/<int:pk>/update/', views.PostUpdate.as_view(), name='new_update'),
   path('news/<int:pk>/delete/', views.PostDelete.as_view(), name='new_delete'),

   path('articles/create/', views.PostCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/update/', views.PostUpdate.as_view(), name='article_update'),
   path('articles/<int:pk>/delete/', views.PostDelete.as_view(), name='article_delete'),
>>>>>>> 17c9f21ccc6e4eff5df1ad86acbf84c87de46949
]
