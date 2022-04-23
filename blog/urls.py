from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('blog', views.PostList.as_view(), name='post_list'),
    path('about', views.AboutView.as_view(), name='about'),
    path('blog/<slug:slug>', views.PostDetails.as_view(), name='post_details'),

]
