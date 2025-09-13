from django.contrib import admin
from .models import Category, News, Contact


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


# admin.site.register(Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']
    search_fields = ['email', 'name']







