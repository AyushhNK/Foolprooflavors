from django.contrib import admin
from .models import RecipePost
from django_summernote.admin import SummernoteModelAdmin

@admin.register(RecipePost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)




