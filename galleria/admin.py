from django.contrib import admin
from .models import Blogger,Photo,tags

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
admin.site.register(Blogger)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(tags)