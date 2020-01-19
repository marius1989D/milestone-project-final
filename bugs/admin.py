from django.contrib import admin
from .models import Bug, Comment

class BugAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'status')
	list_filter = ('status', 'created_on')
	search_fields = ('author', 'title')
	list_editable = ('status',)
	date_hierarchy = ('created_on')




admin.site.register(Bug, BugAdmin)
admin.site.register(Comment)