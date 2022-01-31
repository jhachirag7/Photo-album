from pydoc import describe
from pyexpat.errors import messages
from unicodedata import category
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Category, Photo
import difflib
from django.contrib import messages
from django.contrib.auth.models import auth
# Create your views here.


@login_required(login_url='/accounts/login')
def gallery(request):
    category = Category.objects.filter(user=request.user)
    category_name = list()
    context = {}
    photo = Photo.objects.filter(user=request.user)
    if category.exists():
        for name in category.iterator():
            category_name.append(name)
        context = {
            'category': category_name,
            'photos': photo
        }
    return render(request, 'photos/gallery.html', context=context)


class viewPhoto(View):
    def get(self, request, pk):
        photo = Photo.objects.get(id=pk)
        return render(request, 'photos/photo.html', {'photos': photo, 'id': pk})


def addPhoto(request):
    category = Category.objects.filter(user=request.user)
    All_category = Category.objects.all()
    category_name = list()
    category_name_list = list()
    context = {}
    if category.exists():
        for name in category.iterator():
            category_name.append(name)
            category_name_list.append(name.name)
        context = {
            'category': category_name,
        }
    if request.method == "POST":
        image = request.FILES['image']
        user_category = request.POST['category_new']
        user_select_category = request.POST['category']
        description = request.POST['description']

        if user_select_category != 'none':
            user_category = Category.objects.get(id=user_select_category)
        elif user_category != '':
            user_category = user_category.capitalize()
            similar = difflib.get_close_matches(
                user_category, category_name_list)
            if len(similar) > 0:
                messages.warning(request, 'Are you looking for ' +
                                 similar[0]+' it\'s already a category')
                return render(request, 'photos/add.html', context=context)
            else:
                try:
                    X = All_category.get(name=user_category)
                    X.user.add(request.user)
                except:
                    new_category = Category.objects.create(
                        name=user_category)
                    new_category.user.add(request.user)
                    user_category = new_category
        else:
            messages.warning(request, 'No category selected or created')
            return render(request, 'photos/add.html', context=context)

        photo = Photo.objects.create(
            user=request.user, category=user_category, description=description, image=image)

        return redirect('gallery')

    return render(request, 'photos/add.html', context=context)


class filter(View):
    def get(self, request, id):
        category = Category.objects.filter(user=request.user)
        category_name = list()
        context = {}
        photo = Photo.objects.filter(user=request.user, category=id)
        if category.exists():
            for name in category.iterator():
                category_name.append(name)
        context = {
            'category': category_name,
            'photos': photo
        }
        print(photo)
        return render(request, 'photos/gallery.html', context)


class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect("login")


class Delete(View):
    def get(self, request, pk):
        photo = Photo.objects.get(id=pk)
        photo.delete()
        return redirect("gallery")
