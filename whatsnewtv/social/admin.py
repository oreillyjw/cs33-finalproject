from django.contrib import admin
from .models import Comment, MovieDBInfo,Favorites, Tags

# Register your models here.
# class MenusAdmin(admin.ModelAdmin):
#     search_fields = ('item', 'type' )

admin.site.register(Comment)
admin.site.register(MovieDBInfo)
admin.site.register(Favorites)
admin.site.register(Tags)
