import imp
from django.urls import path
from .views import gallery, viewPhoto, addPhoto, filter, Logout,Delete
urlpatterns = [
    path("", gallery, name="gallery"),
    path("photo/<str:pk>/", viewPhoto.as_view(), name="photo"),
    path("add/", addPhoto, name="add"),
    path("filter/<str:id>", filter.as_view(), name="filter"),
    path("logout", Logout.as_view(), name="logout"),
    path("delete/<str:pk>/", Delete.as_view(), name="delete"),


]
