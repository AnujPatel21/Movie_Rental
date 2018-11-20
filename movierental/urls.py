from django.urls import path

from . import views

urlpatterns = [
    path('available/', views.available,name = 'available'),
    path('rental/', views.rental,name = 'rental'),
    path('movies/', views.movies,name = 'movies'),
    path('customers/', views.customers,name = 'customers'),
    path('addmovie/', views.addmovie,name = 'addmovie'),
    path('addcustomer/', views.addcustomer,name = 'addcustomer'),
    path('remove/<int:num>', views.remove,name = 'remove'),
    path('removee/<int:no>', views.removee,name = 'removee'),
]
