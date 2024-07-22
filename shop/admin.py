from django.contrib import admin
from .models import Frame, Seat, Tire, Basket, Bike, Order


class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'frame', 'tire', 'seat', 'has_basket')
    search_fields = ['name']
    ordering = ('name',)
    list_filter = ('frame', 'tire', 'seat', 'has_basket',)


class TireAdmin(admin.ModelAdmin):
    list_display = ('type', 'quantity')
    search_fields = ['type']
    ordering = ('type',)


class SeatAdmin(admin.ModelAdmin):
    list_display = ('color', 'quantity')
    search_fields = ['color']
    ordering = ('color',)


class FrameAdmin(admin.ModelAdmin):
    list_display = ('color', 'quantity')
    search_fields = ['color']
    ordering = ('color',)


class BasketAdmin(admin.ModelAdmin):
    list_display = ('quantity',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'bike_name', 'name', 'surname', 'phone_number',)
    search_fields = ['id', 'name', 'surname', 'bike__name', 'phone_number']
    ordering = ('id',)
    list_filter = ('status', 'bike__name',)


admin.site.register(Tire, TireAdmin)
admin.site.register(Frame, FrameAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Bike, BikeAdmin)
admin.site.register(Order, OrderAdmin)

