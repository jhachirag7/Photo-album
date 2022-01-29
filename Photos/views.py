from unicodedata import category
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Category, Photo
# Create your views here.


@login_required(login_url='/accounts/login')
def gallery(request):
    category = Category.objects.filter(user=request.user)
    category_name = list()
    context = {}
    photo = Photo.objects.filter(user=request.user)
    print(photo)
    if category.exists():
        for name in category.iterator():
            category_name.append(name.name)
        context = {
            'category': category_name,
            'photos': photo
        }
    return render(request, 'photos/gallery.html', context=context)


class viewPhoto(View):
    def get(self, request, pk):
        photo = Photo.objects.get(id=pk)
        return render(request, 'photos/photo.html', {'photos': photo})


class addPhoto(View):
    def get(self, request):
        return render(request, 'photos/add.html')
