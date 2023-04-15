from django.contrib import admin
from .models import SiteData,MaterialsData,RentMachineryData,TransportData,LabourData,LabourAttendance,StockData,IncomeData,ExpenseData,WorkProgreeData,MachineryPurchaseData,ContactData

class SiteDataAdmin(admin.ModelAdmin):
    list_display = ["manager_id","site_name"]

class MaterialsDataAdmin(admin.ModelAdmin):
    list_display = ["manager_id","Date","site_id","site_name","Material_name","actual_qty"]

class RentMachineryDataAdmin(admin.ModelAdmin):
    list_display = ["manager_id","Date","site_id","site_name","machinery_name","days","Amount"]

class TransportDataAdmin(admin.ModelAdmin):
    list_display = ["manager_id","Date","site_id","site_name","vehical_number","Material_name","kilometer","Amount","Deliver_from","Deliver_To"]

class LabourDataAdmin(admin.ModelAdmin):
    list_display = ["manager_id","labour_name","site_id","site_name","labour_age","labour_gender","salary"]

class StockDataAdmin(admin.ModelAdmin):
    list_display = ["manager_id","site_id","site_name","actual_qty","Material_name"]

class IncomeDataAdmin(admin.ModelAdmin):
    list_display = ["manager_id","Date","Time","payment_mode","payee_name","Amount"]

class ExpenseDataAdmin(admin.ModelAdmin):
    list_display = ["manager_id","Date","Time","payment_mode","payee_name","Amount"]

class WorkProgreeDataAdmin(admin.ModelAdmin):
    list_display = ["manager_id","Date","site_id","site_name","labour_id","labour_name","Work_progress"]

class MachineryPurchaseDataAdmin(admin.ModelAdmin):
    list_display = ["manager_id","Date","site_id","site_name","machinery_name","Rate"]

class LabourAttendanceAdmin(admin.ModelAdmin):
    list_display = ["manager_id","Date","site_id","site_name","labour_id","labour_name"]

class ContactDataAdmin(admin.ModelAdmin):
    list_display = ["name","email","phone_num","message"]

admin.site.register(SiteData,SiteDataAdmin)
admin.site.register(MaterialsData,MaterialsDataAdmin)
admin.site.register(RentMachineryData,RentMachineryDataAdmin)
admin.site.register(TransportData,TransportDataAdmin)
admin.site.register(LabourData,LabourDataAdmin)
admin.site.register(LabourAttendance,LabourAttendanceAdmin)
admin.site.register(StockData,StockDataAdmin)
admin.site.register(IncomeData,IncomeDataAdmin)
admin.site.register(ExpenseData,ExpenseDataAdmin)
admin.site.register(WorkProgreeData,WorkProgreeDataAdmin)
admin.site.register(MachineryPurchaseData,MachineryPurchaseDataAdmin)
admin.site.register(ContactData,ContactDataAdmin)