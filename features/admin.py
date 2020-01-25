from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Feature, Comment

class FeatureAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'status')
	list_filter = ('status', 'created_on')
	search_fields = ('author', 'title')
	list_editable = ('status',)
	date_hierarchy = ('created_on')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'created_on')
	list_filter = ('active', 'created_on')
	search_fields = ('name', 'email')
	date_hierarchy = ('created_on')

admin.site.register(Feature, FeatureAdmin)
admin.site.register(Comment, CommentAdmin)