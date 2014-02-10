from django.contrib import admin
from comics.models import Book, Series, Contributor

admin.site.register(Book)
admin.site.register(Series)
admin.site.register(Contributor)