from django.db import models
from django.forms import ModelForm
from django import forms

GENRE_CHOICES = (
    ('ACTION', 'Action'),
    ('COMEDY', 'Comedy'),
    ('ROMANCE', 'Romance'),
    ('HORROR', 'Horror'),
    ('THRILLER', 'Thriller'),
)
class Movie(models.Model):
    ACTION = 'ACTION'
    COMEDY = 'COMEDY'
    ROMANCE = 'ROMANTIC'
    HORROR = 'HORROR'
    THRILLER = 'THRILLER'

    name = models.CharField(max_length = 200)
    released = models.DateField('date released')
    duration = models.TimeField()
    price = models.FloatField()

    genre = models.CharField(
        choices = GENRE_CHOICES,
        default = ACTION,
        max_length = 20
    )
    rentedby = models.ForeignKey('Customer', on_delete=models.SET_NULL,null=True)
    class Meta:
        db_table = "Movies"

class Customer(models.Model):

    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 15)
    address = models.CharField(max_length = 200)
    age = models.IntegerField()

    class Meta:
        db_table = "Customer"

class movieform(forms.Form):
     name = forms.CharField(label='Movie Name', max_length=50)
     released = forms.DateField(label='Released On')
     duration = forms.TimeField(label='Duration')
     price = forms.FloatField(label='Price')
     genre = forms.CharField(label='Genre',max_length='15',widget = forms.Select(choices = GENRE_CHOICES))

class customerform(ModelForm):
     class Meta:
         model = Customer
         fields = "__all__"
