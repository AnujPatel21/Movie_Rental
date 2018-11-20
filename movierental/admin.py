from django.contrib import admin
from . models import Movie
from . models import Customer

admin.site.register(Movie)
admin.site.register(Customer)
