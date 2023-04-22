from django.db import models
import datetime


class SiteData(models.Model):
    id = models.AutoField
    manager_id = models.TextField(max_length=100,default="")
    manager_name = models.TextField(max_length=100,default="")
    site_name = models.TextField(max_length=100,default="")
    

class MaterialsData(models.Model):
    id = models.AutoField
    Date = models.DateField(default=datetime.date.today)
    manager_id = models.TextField(max_length=100,default="")
    manager_name = models.TextField(max_length=100,default="")
    site_id = models.IntegerField(default=0)
    site_name = models.TextField(max_length=100,default="")
    Material_name = models.TextField(max_length=100,default="")
    work_details = models.TextField(max_length=200,default="")
    actual_qty = models.IntegerField(default=0)
    Remarks = models.TextField(max_length=100,default="")

    def DtypesMaterial():
        mylist = ["Date","manager_id","site_id","site_name","Material_name","work_details","actual_qty","Remarks"]
        main_list = []
        for i in mylist:
            data_type = type(MaterialsData._meta.get_field(i))
            mydic = {}
            if str(data_type) == "<class 'django.db.models.fields.DateField'>":
                mydic["column"] = i
                mydic["dtype"] = "date"
            elif str(data_type) == "<class 'django.db.models.fields.TextField'>":
                mydic["column"] = i
                mydic["dtype"] = "text"
            elif str(data_type) == "<class 'django.db.models.fields.TimeField'>":
                mydic["column"] = i
                mydic["dtype"] = "time"
            elif str(data_type) == "<class 'django.db.models.fields.IntegerField'>":
                mydic["column"] = i
                mydic["dtype"] = "number"
            main_list.append(mydic)
        return main_list

class RentMachineryData(models.Model):
    id = models.AutoField
    manager_id = models.TextField(max_length=100,default="")
    manager_name = models.TextField(max_length=100,default="")
    Date = models.DateField(default=datetime.date.today)
    site_id = models.IntegerField(default=0)
    site_name = models.TextField(max_length=100,default="")
    work_details = models.TextField(max_length=100,default="")
    machinery_name = models.TextField(max_length=100,default="")
    days = models.IntegerField(default=0)
    Amount = models.IntegerField(default=0)

    def DtypesMaterial():
        mylist = ["Date","manager_id","site_id","site_name","machinery_name","work_details","days","Amount"]
        main_list = []
        for i in mylist:
            data_type = type(RentMachineryData._meta.get_field(i))
            mydic = {}
            if str(data_type) == "<class 'django.db.models.fields.DateField'>":
                mydic["column"] = i
                mydic["dtype"] = "date"
            elif str(data_type) == "<class 'django.db.models.fields.TextField'>":
                mydic["column"] = i
                mydic["dtype"] = "text"
            elif str(data_type) == "<class 'django.db.models.fields.TimeField'>":
                mydic["column"] = i
                mydic["dtype"] = "time"
            elif str(data_type) == "<class 'django.db.models.fields.IntegerField'>":
                mydic["column"] = i
                mydic["dtype"] = "number"
            main_list.append(mydic)
        return main_list

class TransportData(models.Model):
    id = models.AutoField
    manager_id = models.TextField(max_length=100,default="")
    manager_name = models.TextField(max_length=100,default="")
    Date = models.DateField(default=datetime.date.today)
    site_id = models.IntegerField(default=0)
    site_name = models.TextField(max_length=100,default="")
    vehical_number = models.TextField(max_length=100,default="")
    Material_name = models.TextField(max_length=100,default="")
    kilometer = models.IntegerField(default=0)
    Amount = models.IntegerField(default=0)
    Deliver_from = models.TextField(max_length=100,default="")
    Deliver_To = models.TextField(max_length=100,default="")


    def DtypesMaterial():
        mylist = ["Date","manager_id","site_id","site_name","vehical_number","kilometer","Material_name","Amount","Deliver_from","Deliver_To"]
        main_list = []
        for i in mylist:
            data_type = type(TransportData._meta.get_field(i))
            mydic = {}
            if str(data_type) == "<class 'django.db.models.fields.DateField'>":
                mydic["column"] = i
                mydic["dtype"] = "date"
            elif str(data_type) == "<class 'django.db.models.fields.TextField'>":
                mydic["column"] = i
                mydic["dtype"] = "text"
            elif str(data_type) == "<class 'django.db.models.fields.TimeField'>":
                mydic["column"] = i
                mydic["dtype"] = "time"
            elif str(data_type) == "<class 'django.db.models.fields.IntegerField'>":
                mydic["column"] = i
                mydic["dtype"] = "number"
            main_list.append(mydic)
        return main_list

class LabourData(models.Model):
    id = models.AutoField
    manager_id = models.TextField(max_length=100,default="")
    manager_name = models.TextField(max_length=100,default="")
    labour_name = models.TextField(max_length=100,default="")
    site_id = models.IntegerField(default=0)
    site_name = models.TextField(max_length=100,default="")
    labour_age = models.IntegerField(default=0)
    labour_gender = models.TextField(max_length=50,default="")
    salary = models.IntegerField(default=0)
    work_details = models.TextField(max_length=200,default="")

    def DtypesMaterial():
        mylist = ["labour_name","manager_id","site_id","site_name","labour_age","labour_gender","salary","work_details"]
        main_list = []
        for i in mylist:
            data_type = type(LabourData._meta.get_field(i))
            mydic = {}
            if str(data_type) == "<class 'django.db.models.fields.DateField'>":
                mydic["column"] = i
                mydic["dtype"] = "date"
            elif str(data_type) == "<class 'django.db.models.fields.TextField'>":
                mydic["column"] = i
                mydic["dtype"] = "text"
            elif str(data_type) == "<class 'django.db.models.fields.TimeField'>":
                mydic["column"] = i
                mydic["dtype"] = "time"
            elif str(data_type) == "<class 'django.db.models.fields.IntegerField'>":
                mydic["column"] = i
                mydic["dtype"] = "number"
            main_list.append(mydic)
        return main_list
    


class StockData(models.Model):
    id = models.AutoField
    manager_id = models.TextField(max_length=100,default="")
    manager_name = models.TextField(max_length=100,default="")
    site_id = models.IntegerField(default=0)
    site_name = models.TextField(max_length=100,default="")
    actual_qty = models.IntegerField(default=0)
    Material_name = models.TextField(max_length=100,default="")

    def DtypesMaterial():
        mylist = ["manager_id","site_id","site_name","actual_qty","Material_name"]
        main_list = []
        for i in mylist:
            data_type = type(StockData._meta.get_field(i))
            mydic = {}
            if str(data_type) == "<class 'django.db.models.fields.DateField'>":
                mydic["column"] = i
                mydic["dtype"] = "date"
            elif str(data_type) == "<class 'django.db.models.fields.TextField'>":
                mydic["column"] = i
                mydic["dtype"] = "text"
            elif str(data_type) == "<class 'django.db.models.fields.TimeField'>":
                mydic["column"] = i
                mydic["dtype"] = "time"
            elif str(data_type) == "<class 'django.db.models.fields.IntegerField'>":
                mydic["column"] = i
                mydic["dtype"] = "number"
            main_list.append(mydic)
        return main_list
    

class IncomeData(models.Model):
    id = models.AutoField
    manager_id = models.TextField(max_length=100,default="")
    manager_name = models.TextField(max_length=100,default="")
    Date = models.DateField(default=datetime.date.today)
    Time = models.TimeField(default=datetime.datetime.now())
    payment_mode = models.TextField(max_length=100,default="")
    payee_name = models.TextField(max_length=100,default="")
    Amount = models.IntegerField(default=0)
    Remark = models.TextField(max_length=100,default="")

    def DtypesMaterial():
        mylist = ["Date","manager_id","Time","payment_mode","payee_name","Amount","Remark"]
        main_list = []
        for i in mylist:
            data_type = type(IncomeData._meta.get_field(i))
            mydic = {}
            if str(data_type) == "<class 'django.db.models.fields.DateField'>":
                mydic["column"] = i
                mydic["dtype"] = "date"
            elif str(data_type) == "<class 'django.db.models.fields.TextField'>":
                mydic["column"] = i
                mydic["dtype"] = "text"
            elif str(data_type) == "<class 'django.db.models.fields.TimeField'>":
                mydic["column"] = i
                mydic["dtype"] = "time"
            elif str(data_type) == "<class 'django.db.models.fields.IntegerField'>":
                mydic["column"] = i
                mydic["dtype"] = "number"
            main_list.append(mydic)
        return main_list
    
    

class ExpenseData(models.Model):
    id = models.AutoField
    manager_id = models.TextField(max_length=100,default="")
    manager_name = models.TextField(max_length=100,default="")
    Date = models.DateField(default=datetime.date.today)
    Time = models.TimeField(default=datetime.datetime.now())
    payment_mode = models.TextField(max_length=100,default="")
    payee_name = models.TextField(max_length=100,default="")
    Amount = models.IntegerField(default=0)
    Remark = models.TextField(max_length=100,default="")

    def DtypesMaterial():
        mylist = ["Date","manager_id","Time","payment_mode","payee_name","Amount","Remark"]
        main_list = []
        for i in mylist:
            data_type = type(ExpenseData._meta.get_field(i))
            mydic = {}
            if str(data_type) == "<class 'django.db.models.fields.DateField'>":
                mydic["column"] = i
                mydic["dtype"] = "date"
            elif str(data_type) == "<class 'django.db.models.fields.TextField'>":
                mydic["column"] = i
                mydic["dtype"] = "text"
            elif str(data_type) == "<class 'django.db.models.fields.TimeField'>":
                mydic["column"] = i
                mydic["dtype"] = "time"
            elif str(data_type) == "<class 'django.db.models.fields.IntegerField'>":
                mydic["column"] = i
                mydic["dtype"] = "number"
            main_list.append(mydic)
        return main_list
    

class WorkProgreeData(models.Model):
    id = models.AutoField
    manager_id = models.TextField(max_length=100,default="")
    manager_name = models.TextField(max_length=100,default="")
    Date = models.DateField(default=datetime.date.today)
    site_id = models.IntegerField(default=0)
    site_name = models.TextField(max_length=100,default="")
    work_details = models.TextField(max_length=100,default="")
    labour_id = models.IntegerField(default=0)
    labour_name = models.TextField(max_length=100,default="")
    Work_progress = models.TextField(max_length=100,default="")
    Remark = models.TextField(max_length=100,default="")

    def DtypesMaterial():
        mylist = ["Date","manager_id","site_id","site_name","labour_id","work_details","labour_name","Work_progress","Remark"]
        main_list = []
        for i in mylist:
            data_type = type(WorkProgreeData._meta.get_field(i))
            mydic = {}
            if str(data_type) == "<class 'django.db.models.fields.DateField'>":
                mydic["column"] = i
                mydic["dtype"] = "date"
            elif str(data_type) == "<class 'django.db.models.fields.TextField'>":
                mydic["column"] = i
                mydic["dtype"] = "text"
            elif str(data_type) == "<class 'django.db.models.fields.TimeField'>":
                mydic["column"] = i
                mydic["dtype"] = "time"
            elif str(data_type) == "<class 'django.db.models.fields.IntegerField'>":
                mydic["column"] = i
                mydic["dtype"] = "number"
            main_list.append(mydic)
        return main_list
    

class MachineryPurchaseData(models.Model):
    id = models.AutoField
    manager_id = models.TextField(max_length=100,default="")
    manager_name = models.TextField(max_length=100,default="")
    Date = models.DateField(default=datetime.date.today)
    site_id = models.IntegerField(default=0)
    site_name = models.TextField(max_length=100,default="")
    machinery_name = models.TextField(max_length=100,default="")
    Rate = models.IntegerField(default=0)
    Remark = models.TextField(max_length=100,default="")

    def DtypesMaterial():
        mylist = ["Date","manager_id","site_id","site_name","machinery_name","Rate","Remark"]
        main_list = []
        for i in mylist:
            data_type = type(MachineryPurchaseData._meta.get_field(i))
            mydic = {}
            if str(data_type) == "<class 'django.db.models.fields.DateField'>":
                mydic["column"] = i
                mydic["dtype"] = "date"
            elif str(data_type) == "<class 'django.db.models.fields.TextField'>":
                mydic["column"] = i
                mydic["dtype"] = "text"
            elif str(data_type) == "<class 'django.db.models.fields.TimeField'>":
                mydic["column"] = i
                mydic["dtype"] = "time"
            elif str(data_type) == "<class 'django.db.models.fields.IntegerField'>":
                mydic["column"] = i
                mydic["dtype"] = "number"
            main_list.append(mydic)
        return main_list
    

class LabourAttendance(models.Model):
    id = models.AutoField
    manager_id = models.TextField(max_length=100,default="")
    manager_name = models.TextField(max_length=100,default="")
    Date = models.DateField(default=datetime.date.today)
    site_id = models.IntegerField(default=0)
    site_name = models.TextField(max_length=100,default="")
    work_details = models.TextField(max_length=100,default="")
    labour_id = models.IntegerField(default=0)
    labour_name = models.TextField(max_length=100,default="")

    def DtypesMaterial():
        mylist = ["Date","manager_id","site_id","site_name","labour_id","work_details","labour_name"]
        main_list = []
        for i in mylist:
            data_type = type(LabourAttendance._meta.get_field(i))
            mydic = {}
            if str(data_type) == "<class 'django.db.models.fields.DateField'>":
                mydic["column"] = i
                mydic["dtype"] = "date"
            elif str(data_type) == "<class 'django.db.models.fields.TextField'>":
                mydic["column"] = i
                mydic["dtype"] = "text"
            elif str(data_type) == "<class 'django.db.models.fields.TimeField'>":
                mydic["column"] = i
                mydic["dtype"] = "time"
            elif str(data_type) == "<class 'django.db.models.fields.IntegerField'>":
                mydic["column"] = i
                mydic["dtype"] = "number"
            main_list.append(mydic)
        return main_list
    

class ContactData(models.Model):
    id = models.AutoField
    name = models.TextField(max_length=100,default="")
    email = models.EmailField(max_length=100,default="")
    phone_num = models.IntegerField(default=0)
    message = models.TextField(max_length=500,default="")
