from django.contrib import admin
from .models import Topic, Response

# in the admin site, register the album... Thus, the album will show up in the admin site 
admin.site.register(Topic)
admin.site.register(Response)