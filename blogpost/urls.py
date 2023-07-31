from django.urls import path
from django.contrib.auth import views

from blogpost import views

urlpatterns = [
    # path('', views.userlogin, name='login'),
    path('', views.index, name='index'),
    path('blog/detail/<int:post_id>/', views.detail, name='detail'),
    path('blog/contact_us/', views.contact_us, name='contact_us'),
    path('blog/about_us/', views.about_us, name='about_us'),
    path('<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/add_reply/', views.add_reply, name='add_reply'),
]
