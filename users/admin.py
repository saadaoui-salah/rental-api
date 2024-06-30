from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Favorites)
admin.site.register(State)
admin.site.register(SavedSearch)