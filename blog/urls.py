from django.urls import path
from . import views
urlpatterns= [
path("<int:blog_id>" , views.single_page_blog ,name ='blog_id'),
path("", views.blog , name = 'home'),
]