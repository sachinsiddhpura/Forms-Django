from django.contrib import admin

# Register your models here.
from .models import PersonType, Person

admin.site.register(PersonType)
admin.site.register(Person)
