from django.urls import path
from . import views
urlpatterns = [
    path("", views.gallery.as_view(), name="gallery"),
    path("photo/<str:pk>/", views.viewPhoto.as_view(), name="photo"),
    path("add/", views.addPhoto.as_view(), name="add"),

]
