from django.contrib import admin
from .models import ImagePost, ImageLocation,ImageCategory

# Register your models here.
admin.site.register(ImagePost)
admin.site.register(ImageLocation)
admin.site.register(ImageCategory)


