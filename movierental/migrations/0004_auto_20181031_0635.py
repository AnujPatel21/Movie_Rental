# Generated by Django 2.1.2 on 2018-10-31 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierental', '0003_movie_rented'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('ACTION', 'Action'), ('COMEDY', 'Comedy'), ('ROMANTIC', 'Romance'), ('HORROR', 'Horror'), ('THRILLER', 'Thriller')], default='ACTION', max_length=20),
        ),
    ]