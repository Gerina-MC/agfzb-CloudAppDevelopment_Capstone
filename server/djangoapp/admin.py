from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display=("make", "name", "dealer_id", "type_c", "year")
    list_filter = ["year"]
    search_fields = ["name", "type_c"]


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ("name", "description")


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
