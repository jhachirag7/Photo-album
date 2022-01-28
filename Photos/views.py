from django.shortcuts import render
from django.views import View
# Create your views here.


class gallery(View):
    def get(self, request):
        return render(request, 'photos/gallery.html')


class viewPhoto(View):
    def get(self, request, pk):
        return render(request, 'photos/photo.html')


class addPhoto(View):
    def get(self, request):
        return render(request, 'photos/add.html')
