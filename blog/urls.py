from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.posts, name='posts'),
    # ffpath('post/<slug:slug>', views.post_detail, name='post-detail'),
]


