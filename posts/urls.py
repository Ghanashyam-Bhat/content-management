from django.urls import path, re_path
from . import views

urlpatterns = [
    path("personal/", views.myPosts),
    path("<str:id>/", views.postDetails),
    path("new/", views.createpost),
]
