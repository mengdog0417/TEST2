from django.db import models
from django.utils import timezone

class Employee(models.Model): #客戶
    number = models.CharField(max_length=20,verbose_name='id', unique=True)
    serial = models.CharField(max_length=50,default=None)
    pwd = models.CharField(max_length=50,default=None)
    def __str__(self):
        return self.number
    
class Machine(models.Model):
    LEAVE = (
        ('1','1'), #前面是展示在前端界面的内容,后面的'first'是真正存在数据库中的
        ('2','2'),
        ('3','3'),
    )
    number = models.CharField(max_length=20,verbose_name='id')
    serial = models.CharField(max_length=50,default=None)
    cotter_number = models.CharField(max_length=1,choices=LEAVE)

class Customers(models.Model):
    number = models.CharField(max_length=20,verbose_name='id', unique=True)
    name = models.CharField(max_length=50,default=None)
    def __str__(self):
        return self.number

class Product(models.Model):
    number = models.CharField(max_length=20,verbose_name='id', unique=True)
    name = models.CharField(max_length=50,default=None)
    def __str__(self):
        return self.number

class Transfer_doc(models.Model):
    number = models.CharField(max_length=20,verbose_name='id', unique=True)
    customer_id =models.ForeignKey(Customers, on_delete=models.CASCADE)
    product_id =models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.number


class Sinter_process(models.Model):
    SELVALUE = (
        ('EARLY','EARLY'), #前面是展示在前端界面的内容,后面的'first'是真正存在数据库中的
        ('MIDDIE','MIDDIE'),
        ('EARLY','EARLY'),
    )
    LEAVE = (
        ('1','1'), #前面是展示在前端界面的内容,后面的'first'是真正存在数据库中的
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
    number = models.CharField(max_length=20,verbose_name='id')
    transfer_doc_id = models.ForeignKey(Transfer_doc, on_delete=models.CASCADE)
    stage_id =  models.CharField(max_length=20,  choices=SELVALUE, default='EARLY')
    layer = models.CharField(max_length=20,  choices=LEAVE, default='1')
    A = models.CharField(max_length=50,default=None)
    B = models.CharField(max_length=50,default=None)
    check_employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_time= models.DateTimeField('check_time', default=timezone.now)

# class Restaurant(models.Model):
#     name = models.CharField(max_length=20,verbose_name='部门名', help_text='一个部门的名字应该唯一', unique=True, db_index=True)
#     phone_number = models.CharField(max_length=15)
#     address = models.CharField(max_length=50, blank=True)
#     addressc = models.CharField(max_length=50, blank=True)

# class Food(models.Model):
#     name = models.CharField(max_length=20)
#     price = models.DecimalField(max_digits=3, decimal_places=0)
#     comment = models.CharField(max_length=50, blank=True)
#     is_spicy = models.BooleanField()
#     name1 = models.CharField(max_length=20)
#     # name3 = models.CharField(max_length=20)
#     # update_time = models.DateTimeField('更新时间', auto_now=True)
#     # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     update_time = models.DateTimeField('更新时间', default=timezone.now)

# class Coding(models.Model):
#     text = models.CharField(max_length=10)
#     gender = models.IntegerField(unique=True,primary_key = True)

# class List(models.Model):
#     Number = models.IntegerField(unique=True,blank=False, null=False)
#     Gender = models.ForeignKey('Coding',on_delete=models.CASCADE)