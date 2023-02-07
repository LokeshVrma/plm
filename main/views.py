from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import ItemForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
import datetime as dt


# Create your views here.
@unauthenticated_user
def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return HttpResponse("You are not authorised")

    year = dt.date.today().year    
    context = {
        'year': year
    }
    return render(request, 'main/login.html', context)

def LogoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    item_detail = Item.objects.all().order_by('item_name')
    query = request.GET.get('query')
    if query is not '' and query is not None:
        item_detail = item_detail.filter(item_name__icontains=query)

    year = dt.date.today().year
    context = {
        'item_detail': item_detail,
        'year': year
    }

    return render(request, 'main/home.html', context)

@login_required(login_url='login')
def createItem(request):
    form  = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    context = {
        'form': form
    }
    print()
    return render(request, 'main/create_item.html', context)

@login_required(login_url='login')
def updateItem(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            print(form.errors)
    context = {
        'form': form
    }
    
    return render(request, 'main/update_item.html', context)

@login_required(login_url='login')
def deleteItem(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect(home)

    context = {
        'item': item
    }
    return render(request, 'main/delete_item.html', context)

@login_required(login_url='login')
def itemDetail(request, pk):
    item = Item.objects.get(id=pk)
    context = {
        'item': item
    }
    return render(request, 'main/item_detail.html', context)