from django.contrib import admin
from .models import Bd
from .models import Rubric

#admin.site.register(Bd) #регистрация бд


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published','rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bd,BdAdmin)
admin.site.register(Rubric)