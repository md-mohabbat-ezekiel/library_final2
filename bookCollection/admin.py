from django.contrib import admin
from . import models
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('Name',)}
    list_display = ['Name', 'slug']
    
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.AddBook)
admin.site.register(models.Comment)
admin.site.register(models.BuyBook)
