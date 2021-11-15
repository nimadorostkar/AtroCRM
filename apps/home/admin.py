from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from .models import Product, Customer, Order_request, Order_incomings
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin


admin.site.site_header= " آتـــروتـک "
admin.site.site_title= "AtroCRM"
admin.site.register(LogEntry)







#------------------------------------------------------------------------------
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'price', 'short_description', 'image_tag', 'available')
    list_filter = ("available","date_created")
    search_fields = ['name',]

admin.site.register(models.Product, ProductAdmin)







#------------------------------------------------------------------------------
class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'phone', 'company', 'address', 'short_description')
    list_filter = ("date_created", "product_tag")
    search_fields = ['name',]
    raw_id_fields = ('product_tag',)

admin.site.register(models.Customer, CustomerAdmin)






#------------------------------------------------------------------------------
class Order_incomingsInline(StackedInlineJalaliMixin, TabularInlineJalaliMixin, admin.TabularInline):
    model = Order_incomings
    extra = 1


class Order_requestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('product','user','customer','short_description','status')
    list_filter = ("user", 'product','status', 'date_created')
    search_fields = ['product__name']
    raw_id_fields = ('product', 'user', 'customer')
    inlines = [ Order_incomingsInline, ]



admin.site.register(models.Order_request, Order_requestAdmin)














# End
