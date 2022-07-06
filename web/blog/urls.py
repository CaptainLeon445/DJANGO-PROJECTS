from django.urls import path,re_path
from blog import views
app_name='blog'
urlpatterns=[
    path('',views.PostList,name='postlist'),
    path('<slug:slug>/tag/',views.PostList,name='post_list_by_category'),
    path('<slug:tag_slug>/',views.PostList,name='post_list_by_tag'),
    path('<int:id>/<slug:slug>/',views.PostDetail,name='postdetail'),
    path('<int:post_id>/<slug:post_slug>/share/', views.post_share, name='post_share'),
]


