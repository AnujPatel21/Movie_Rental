from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Customer
from . models import Movie
from . models import movieform, customerform
from django.http import HttpResponseRedirect
from django.shortcuts import render


def available(request):
    availables = Movie.objects.all().filter(rentedby__isnull = False)
    return render(request, "available.html", {'movies':availables})

def rental(request):
    rentals = Movie.objects.all().filter(rentedby__isnull = True)
    return render(request, "rental.html", {'movies':rentals})

def movies(request):
    movies = Movie.objects.all()
    return render(request, "movies.html", {'movies': movies,})

def customers(request):
    customers = Customer.objects.all()
    return render(request, "customers.html", {'customers': customers,})

def addmovie(request):
    if request.method == 'POST':
        form = movieform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            released = form.cleaned_data['released']
            duration = form.cleaned_data['duration']
            price = form.cleaned_data['price']
            genre = form.cleaned_data['genre']
            abc = Movie(name = name, released = released, duration = duration, price = price, genre = genre)
            abc.save()
            return HttpResponseRedirect('/movierental/movies/')
    else:
        form = movieform()
    return render(request, 'addmovie.html', {'movieform': form})

def addcustomer(request):
    form2 = customerform(request.POST)
    if form2.is_valid():
        form2.save()
        return HttpResponseRedirect('/movierental/customers/')
    return render(request, "addcustomer.html", {'customerform' : form2})

def remove(request,num):
    abc = Movie.objects.get(id = num)
    abc.delete()
    return redirect('movies')

def removee(request,no):
    cust = Customer.objects.get(id = no)
    cust.delete()
    return redirect('customers')
