from django.urls import path, re_path
from . import views

urlpatterns = [
    path("personal/", views.myPosts),
    path("new/", views.createpost),
    path("edit/<str:id>/", views.createpost),
    path("<int:id>/", views.postDetails),
]
