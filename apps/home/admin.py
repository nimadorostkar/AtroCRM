from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry
from .models import Product, Customer, Order_request, Order_steps
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from mptt.admin import MPTTModelAdmin, TreeRelatedFieldListFilter, DraggableMPTTAdmin
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
    list_display = ('name', 'phone', 'short_description')
    list_filter = ("date_created", "date_created")
    search_fields = ['name',]
    raw_id_fields = ('product_tag',)

admin.site.register(models.Customer, CustomerAdmin)






#------------------------------------------------------------------------------
class Order_stepsInline(admin.TabularInline):
    model = Order_steps
    extra = 1

class Order_requestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('product','user','customer','short_description','status')
    list_filter = ("user", 'product','status', "customer", 'date_created')
    search_fields = ['product__name']
    raw_id_fields = ('product', 'user', 'customer')
    inlines = [ Order_stepsInline, ]

admin.site.register(models.Order_request, Order_requestAdmin)














# End
