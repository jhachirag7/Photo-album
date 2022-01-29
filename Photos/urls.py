import imp
from django.urls import path
from .views import gallery, viewPhoto, addPhoto
urlpatterns = [
    path("", gallery, name="gallery"),
    path("photo/<str:pk>/", viewPhoto.as_view(), name="photo"),
    path("add/", addPhoto.as_view(), name="add"),

]
