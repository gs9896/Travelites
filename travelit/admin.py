from django.contrib import admin
from .models import Destination, Complaints, Guides
# Register your models here.

admin.site.register(Destination)
admin.site.register(Complaints)
admin.site.register(Guides)