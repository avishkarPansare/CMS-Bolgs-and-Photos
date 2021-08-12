from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignUpForm, LoginForm, BlogForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Blog, Blog_Category, Photo, Photo_Category
# Create your views here.


# about
def about(request):
    return render(request, 'blog/about.html')

# Contact


def contact(request):
    return render(request, 'blog/contact.html')

# Home page


@login_required(login_url='login')
def home(request):
    posts = Blog.objects.all().order_by("-id")
    photos = Photo.objects.all().order_by("-id")
   # print("Photo ========>",photos)
    context = {'Pic': photos, 'posts': posts}
    return render(request, 'blog/home.html', context)


# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                print("====================>", user)
                if user is not None:
                    login(request, user)

                    messages.success(request, 'Logged in Successfully !!')

                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')


# logout function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# user creation form
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations!! You have become an website user.')
            user = form.save()
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        posts = Blog.objects.filter(user=user)
        photos = Photo.objects.filter(user=user)
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html', {'photos': photos, 'posts': posts, 'full_name': full_name, 'groups': gps})
    else:
        return HttpResponseRedirect('/login/')


# 33

# Update/Edit Post


def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Blog.objects.get(pk=id)
            form = BlogForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Blog.objects.get(pk=id)
            form = BlogForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

# Delete Post


def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Blog.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


@login_required(login_url='login')
def deleteOrder(request, pk):
    img = Photo.objects.get(id=pk)

    if request.method == "GET":
        img.delete()
        return redirect('dashboard')


@login_required(login_url='login')
def viewPhoto(request, pk):
    img = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'img': img})





def addPhoto(request):

    categories = Photo_Category.objects.all()
    user1 = request.user
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Photo_Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created =Photo_Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                photo=image,
                user=user1
            )

        return redirect('dashboard')

    context = {'categories': categories}
    return render(request, 'photos/addPhoto.html', context)


def addBlog(request):
    categories = Blog_Category.objects.all()
    user1 = request.user
    if request.method == 'POST':
        data = request.POST
        if data['category'] != 'none':
            category1 = Blog_Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category1, created =Blog_Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None
       # print(data)
       # print('catgory ===============>',category1)
        bolog = Blog.objects.create(Title=data['title'],Category=category1,Oneline=data['oneline'],Content=data['Content'],user=user1)

        return redirect('dashboard')

    context = {'categories': categories}
    return render(request, 'blog/addBlog.html', context)