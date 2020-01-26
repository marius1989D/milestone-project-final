from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineAdminInline(admin.TabularInline):
	model = OrderLineItem

class OrderAdmin(admn.ModelAdmin):
	inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)
