from django.contrib import admin
# from .models import  Restaurant, Food,Coding,List
from .models import  Employee,Machine,Product,Transfer_doc,Customers,Sinter_process
from django.utils import timezone
# from .models import A,Food
# Register your models here.


# class RestaurantAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone_number', 'address')

# class FoodAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price','is_spicy','name1','update_time'] #展示項目
#     list_filter = ('is_spicy',) #設置過濾項目
#     list_per_page =  1 #每頁顯示條數目
#     list_editable = ('price',) #可編輯字段 list_display[0]第一格不能修改

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['number', 'serial','pwd'] #展示項目

class MachineAdmin(admin.ModelAdmin):
    list_display = ['number', 'serial','cotter_number'] #展示項目
    
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['number', 'name'] #展示項目

class ProductAdmin(admin.ModelAdmin):
    list_display = ['number', 'name'] #展示項目

class Transfer_docAdmin(admin.ModelAdmin):
    list_display = ['number', 'customer_id','product_id'] #展示項目

class Sinter_processAdmin(admin.ModelAdmin):
    list_display = ['number', 'transfer_doc_id','stage_id','layer','A','B','check_employee_id','check_time'] #展示項目
    
# admin.site.register(Restaurant, RestaurantAdmin)
# admin.site.register(Food, FoodAdmin)
# admin.site.register([Coding, List])

admin.site.register(Employee,EmployeeAdmin)

admin.site.register(Machine,MachineAdmin)

admin.site.register(Customers,CustomersAdmin)

admin.site.register(Product,ProductAdmin)

admin.site.register(Transfer_doc,Transfer_docAdmin)

admin.site.register(Sinter_process,Sinter_processAdmin)


