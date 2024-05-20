from django.contrib import admin
from .models import Tree
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ( 'tree_name', 'tree_scientific_name','tree_description', 'created_by','search_link_key')
    search_fields = ('tree_name','tree_scientific_name')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()
    

admin.site.register(Tree, AuthorAdmin)