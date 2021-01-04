from django.contrib import admin
from .models import Post, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)
admin.site.register(Category)