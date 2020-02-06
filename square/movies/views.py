from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *

def index(requests):
    all_movies = movie_data.objects.all()
    return render(requests,'movies/index.html',{'all_movies':all_movies,})


def details(requests,movie_id):
    data = get_object_or_404(movie_data, id=movie_id)
    return render(requests, 'movies/details.html', { 'data': data,})


def new_movie(request):
    form = add_new_form()
    if request.method == 'POST':
        form = add_new_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'movies/add_new.html', {'form': form, })



def edit_new_movie(request,id):
    mov = get_object_or_404(movie_data, id=id)
    form = add_new_form(instance=mov)
    if request.method == 'POST':
        form = add_new_form(request.POST, request.FILES, instance=mov)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'movies/edit_add_new.html', {'form': form, 'mov':mov})



def search(request):
    query = ''
    data = ''
    if request.method == 'POST':
        print(request.POST['search'])
        query = request.POST['search']
        data = movie_data.objects.filter(movie_name__contains=request.POST['search'])

    return render(request,'movies/search.html',{'data':data,'query':query})