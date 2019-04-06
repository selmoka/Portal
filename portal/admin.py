from django.contrib import admin
from .models import Event, Person, PersonStatus

# to do: register models for Admin app to use

# Register your models here.

admin.site.register(Event)
admin.site.register(Person)
admin.site.register(PersonStatus)