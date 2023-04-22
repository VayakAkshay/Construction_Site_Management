from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import SiteData,MaterialsData,RentMachineryData,TransportData,LabourData,LabourAttendance,StockData,IncomeData,ExpenseData,WorkProgreeData,MachineryPurchaseData,ContactData

def Loginsystem(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            print("User id = ",request.user.id)
            messages.success(request,"You are logged in successfully")
            return redirect("/")
        else:
            messages.warning(request,"Please Enter Valid username and password.")
        return redirect("/")
    return redirect('/')

def Homepage(request):
    return render(request,"Mainpage/index.html")

def DashboardPage(request):
    income_table = IncomeData.objects.filter(manager_id = request.user.id).all().values()
    expense_data = ExpenseData.objects.filter(manager_id = request.user.id).all().values()
    total_income = 0
    total_expense = 0
    for i in income_table:
        total_income = total_income + i["Amount"]
    for i in expense_data:
        total_expense = total_expense + i["Amount"]
    total = total_income - total_expense
    amount = total_income + total_expense
    return render(request,"Mainpage/dashboard.html",{"total_income":total_income,"total_expense":total_expense,"total":total,"amount":amount})

def SitesPage(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        site_data = SiteData()
        if request.method == "POST":
            site_name = request.POST.get("site_name")
            manager_id = request.user.id
            site_data.site_name = site_name
            site_data.manager_id = manager_id
            site_data.manager_name = request.user.first_name + " " + request.user.last_name
            site_data.save()
            messages.success(request,"Data Added Successfully")
            return redirect("/sites/")
        return render(request,"Mainpage/sites.html",{'sites_data':sites_data,"tab_name":"SiteData","redirect":"/sites/"})
    else:
        return render(request,"Mainpage/sites.html")

def ManageMaterial(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        material_data = MaterialsData.objects.filter(manager_id = request.user.id).all().values()
        if request.method == "POST":
            date = request.POST.get("date")
            site_names = request.POST.get("site_name")
            site_id = site_names.split(",")[0]
            site_name = site_names.split(",")[1]
            details = request.POST.get("details")
            material_name = request.POST.get("material_name")
            qty = request.POST.get("qty")
            remarks = request.POST.get("remarks")
            manager_name = request.user.first_name + " " + request.user.last_name
            material_data = MaterialsData(Date = date,manager_id = request.user.id,manager_name = manager_name,site_id = site_id,site_name = site_name,Material_name = material_name,work_details = details,actual_qty=qty,Remarks=remarks)
            material_data.save()
            messages.success(request,"Data Added Successfully")
            return redirect("/materials/")
        return render(request,"Mainpage/material.html",{"sites_data":sites_data,"material_data":material_data,"tab_name":"MaterialsData","redirect":"/materials/"})
    else:
        return render(request,"Mainpage/material.html")

def ManageMachine(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        machinery_data = RentMachineryData.objects.filter(manager_id = request.user.id).all().values()
        if request.method == "POST":
            date = request.POST.get("date")
            site_names = request.POST.get("site_name")
            site_id = site_names.split(",")[0]
            site_name = site_names.split(",")[1]
            details = request.POST.get("details")
            machinery = request.POST.get("machinery")
            days = request.POST.get("days")
            rate = request.POST.get("rate")
            manager_name = request.user.first_name + " " + request.user.last_name
            amount = int(rate) * int(days)
            rent_data = RentMachineryData(manager_id = request.user.id,manager_name = manager_name,Date=date,site_id=site_id,site_name=site_name,work_details=details,machinery_name=machinery,days=days,Amount = amount)
            rent_data.save()
            messages.success(request,"Data Added Successfully")
            return redirect("/manage-machines/")
        return render(request,"Mainpage/manage-machine.html",{"sites_data":sites_data,"machinery_data":machinery_data,"tab_name":"RentMachineryData","redirect":"/manage-machines/"})
    else:
        return render(request,"Mainpage/manage-machine.html")

def ManageTransport(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        transport_datas = TransportData.objects.filter(manager_id = request.user.id).all().values()
        if request.method == "POST":
            date = request.POST.get("date")
            site_names = request.POST.get("site_name")
            site_id = site_names.split(",")[0]
            site_name = site_names.split(",")[1]
            vehical_num = request.POST.get("vehical_num")
            material = request.POST.get("material")
            km = request.POST.get("km")
            amount = request.POST.get("amount")
            froms = request.POST.get("from")
            to = request.POST.get("to")
            manager_name = request.user.first_name + " " + request.user.last_name
            transport_data = TransportData(manager_id = request.user.id,manager_name = manager_name,Date = date,site_id = site_id,site_name = site_name,vehical_number = vehical_num,Material_name = material,kilometer = km,Amount = amount,Deliver_from = froms,Deliver_To = to)
            transport_data.save()
            messages.success(request,"Data Added Successfully")
            return redirect("/transport/")
        return render(request,"Mainpage/transport.html",{"sites_data":sites_data,"transport_datas":transport_datas,"tab_name":"TransportData","redirect":"/transport/"})
    else:
        return render(request,"Mainpage/transport.html")

def ManageLabour(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        labour_datas = LabourData.objects.filter(manager_id = request.user.id).all().values()
        if request.method == "POST":
            manager_id = request.user.id
            name = request.POST.get("name")
            site_names = request.POST.get("site_name")
            age = request.POST.get("age")
            salary = request.POST.get("salary")
            gender = request.POST.get("gender")
            details = request.POST.get("details")
            site_id = site_names.split(",")[0]
            site_name = site_names.split(",")[1]
            manager_name = request.user.first_name + " " + request.user.last_name
            labout_data = LabourData(manager_id = manager_id,manager_name = manager_name,labour_name = name,site_id = site_id,site_name = site_name,labour_age = age,labour_gender = gender,salary=salary,work_details = details)
            labout_data.save()
            messages.success(request,"Data Added Successfully")
            return redirect('/labour/')
        return render(request,"Mainpage/labour.html",{"sites_data":sites_data,"labour_datas":labour_datas,"tab_name":"LabourData","redirect":"/labour/"})
    else:
        return render(request,"Mainpage/labour.html")

def ManageGodownStocks(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        stock_datas = StockData.objects.filter(manager_id = request.user.id).all().values()
        if request.method == "POST":
            date = request.POST.get("date")
            site_names = request.POST.get("site_name")
            site_id = site_names.split(",")[0]
            site_name = site_names.split(",")[1]
            qty = request.POST.get("qty")
            material = request.POST.get("material")
            manager_name = request.user.first_name + " " + request.user.last_name
            stock_data = StockData(manager_id = request.user.id,manager_name = manager_name,site_id=site_id,site_name=site_name,actual_qty = qty,Material_name = material)
            stock_data.save()
            messages.success(request,"Data Added Successfully")
            return redirect('/godown/')
        return render(request,"Mainpage/godown.html",{"sites_data":sites_data,"stock_datas":stock_datas,"tab_name":"StockData","redirect":"/godown/"})
    else:
        return render(request,"Mainpage/godown.html")

def ManageAccounting(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        profit_datas = IncomeData.objects.filter(manager_id = request.user.id).all().values()
        expense_datas = ExpenseData.objects.filter(manager_id = request.user.id).all().values()
        return render(request,"Mainpage/accounting.html",{"sites_data":sites_data,"profit_datas":profit_datas,"expense_datas":expense_datas,"tab_name1":"IncomeData","redirect":"/accounting/","tab_name2":"ExpenseData"})
    else:
        return render(request,"Mainpage/accounting.html")

def ManageProfit(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        if request.method == "POST":
            date = request.POST.get("date")
            site_names = request.POST.get("site_name")
            time = request.POST.get("time")
            mode = request.POST.get("mode")
            payee = request.POST.get("payee")
            amount = request.POST.get("amount")
            remarks = request.POST.get("remarks")
            manager_name = request.user.first_name + " " + request.user.last_name
            income_data = IncomeData(manager_id = request.user.id,manager_name = manager_name,Date=date,Time=time,payment_mode = mode,payee_name = payee,Amount = amount,Remark = remarks)
            income_data.save()
            messages.success(request,"Data Added Successfully")
            return redirect('/accounting/')
        return render(request,"Mainpage/accounting.html",{"sites_data":sites_data})
    else:
        return render(request,"Mainpage/accounting.html")

def ManageExpenses(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        if request.method == "POST":
            date = request.POST.get("date")
            site_names = request.POST.get("site_name")
            time = request.POST.get("time")
            mode = request.POST.get("mode")
            payee = request.POST.get("payee")
            amount = request.POST.get("amount")
            remarks = request.POST.get("remarks")
            manager_name = request.user.first_name + " " + request.user.last_name
            expense_data = ExpenseData(manager_id = request.user.id,manager_name = manager_name,Date=date,Time=time,payment_mode = mode,payee_name = payee,Amount = amount,Remark = remarks)
            expense_data.save()
            messages.success(request,"Data Added Successfully")
            return redirect('/accounting/')
        return render(request,"Mainpage/accounting.html",{"sites_data":sites_data})
    else:
        return render(request,"Mainpage/accounting.html")
    
def ManageProgress(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        labour_data = LabourData.objects.filter(manager_id = request.user.id).all().values()
        progress_datas = WorkProgreeData.objects.filter(manager_id = request.user.id).all().values()
        if request.method == "POST":
            date = request.POST.get("date")
            site_names = request.POST.get("site_name")
            site_id = site_names.split(",")[0]
            site_name = site_names.split(",")[1]
            details = request.POST.get("details")
            labour_names = request.POST.get("labour_name")
            labour_id = labour_names.split(",")[0]
            labour_name = labour_names.split(",")[1]
            progress = request.POST.get("progress")
            remarks = request.POST.get("remarks")
            manager_name = request.user.first_name + " " + request.user.last_name
            progress_data = WorkProgreeData(manager_id = request.user.id,manager_name = manager_name,Date = date,site_id = site_id,site_name = site_name,work_details = details,labour_id = labour_id,labour_name = labour_name,Work_progress = progress,Remark = remarks)
            progress_data.save()
            messages.success(request,"Data Added Successfully")
            return redirect('/work-progress/')
        return render(request,"Mainpage/progress.html",{"sites_data":sites_data,"labour_data":labour_data,"progress_datas":progress_datas,"tab_name":"WorkProgreeData","redirect":"/work-progress/"})
    else:
        return render(request,"Mainpage/progress.html")

def ManageAttendance(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        labour_data = LabourData.objects.filter(manager_id = request.user.id).all().values()
        attendance_datas = LabourAttendance.objects.filter(manager_id = request.user.id).all().values()
        if request.method == "POST":
            date = request.POST.get("date")
            site_names = request.POST.get("site_name")
            site_id = site_names.split(",")[0]
            site_name = site_names.split(",")[1]
            details = request.POST.get("details")
            labour_names = request.POST.get("labour_name")
            labour_id = labour_names.split(",")[0]
            labour_name = labour_names.split(",")[1]
            manager_name = request.user.first_name + " " + request.user.last_name
            attendance = LabourAttendance(manager_id = request.user.id,manager_name = manager_name,Date = date,site_id = site_id,site_name = site_name,work_details = details,labour_id = labour_id,labour_name=labour_name)
            attendance.save()
            messages.success(request,"Data Added Successfully")
            return redirect("/attendance/")
        return render(request,"Mainpage/attendance.html",{"sites_data":sites_data,"labour_data":labour_data,"attendance_datas":attendance_datas,"tab_name":"LabourAttendance","redirect":"/attendance/"})
    else:
        return render(request,"Mainpage/attendance.html")

def ManageMachinery(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        machinery_datas = MachineryPurchaseData.objects.filter(manager_id = request.user.id).all().values()
        if request.method == "POST":
            date = request.POST.get("date")
            site_names = request.POST.get("site_name")
            site_id = site_names.split(",")[0]
            site_name = site_names.split(",")[1]
            machinery = request.POST.get("machinery")
            rate = request.POST.get("rate")
            remarks = request.POST.get("remarks")
            manager_name = request.user.first_name + " " + request.user.last_name
            buy_machine = MachineryPurchaseData(manager_id = request.user.id,manager_name = manager_name,Date = date,site_id = site_id,site_name = site_name,machinery_name = machinery,Rate=rate,Remark = remarks)
            buy_machine.save()
            messages.success(request,"Data Added Successfully")
            return redirect("/purchase-machine/")
        return render(request,"Mainpage/machinery.html",{"sites_data":sites_data,"machinery_datas":machinery_datas,"tab_name":"MachineryPurchaseData","redirect":"/purchase-machine/"})
    else:
        return render(request,"Mainpage/machinery.html")

def ManageReports(request):
    if request.user.is_authenticated:
        sites_data = SiteData.objects.filter(manager_id = request.user.id).all().values()
        return render(request,"Mainpage/reports.html",{"sites_data":sites_data})
    else:
        return render(request,"Mainpage/reports.html")
    

def ContactManager(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        phone = request.POST.get("phone")
        contact = ContactData(name = name,email = email,phone_num = phone,message = message)
        contact.save()
        messages.success(request,"Your request has been succesfully received")
        return redirect("/")
    return redirect("/")


def DeleteManager(request):
    if request.method == "POST":
        id = request.POST.get("id")
        tab_name = request.POST.get("tab_name")
        redirects = request.POST.get("redirect")
        if tab_name == "SiteData":
            SiteData.objects.filter(id = id).delete()
            return redirect(redirects)
        elif tab_name == "MaterialsData":
            MaterialsData.objects.filter(id = id).delete()
            return redirect(redirects)
        elif tab_name == "RentMachineryData":
            RentMachineryData.objects.filter(id = id).delete()
            return redirect(redirects)
        elif tab_name == "TransportData":
            TransportData.objects.filter(id = id).delete()
            return redirect(redirects)
        elif tab_name == "LabourData":
            LabourData.objects.filter(id = id).delete()
            return redirect(redirects)
        elif tab_name == "LabourAttendance":
            LabourAttendance.objects.filter(id = id).delete()
            return redirect(redirects)
        elif tab_name == "StockData":
            StockData.objects.filter(id = id).delete()
            return redirect(redirects)
        elif tab_name == "IncomeData":
            IncomeData.objects.filter(id = id).delete()
            return redirect(redirects)
        elif tab_name == "ExpenseData":
            ExpenseData.objects.filter(id = id).delete()
            return redirect(redirects)
        elif tab_name == "WorkProgreeData":
            WorkProgreeData.objects.filter(id = id).delete()
            return redirect(redirects)
        elif tab_name == "MachineryPurchaseData":
            MachineryPurchaseData.objects.filter(id = id).delete()
            return redirect(redirects)
        
def UpdateData(request):
    if request.method == "POST":
        id = request.POST.get("id")
        tab_name = request.POST.get("tab_name")
        redirects = request.POST.get("redirect")
        if tab_name == "MaterialsData":
            data = MaterialsData.objects.filter(id = id).values()[0]
            mylist = MaterialsData.DtypesMaterial()
            for i in range(len(mylist)):
                mydic = mylist[i]
                mydic["values"] = data[mydic["column"]]
            return render(request,"Mainpage/updateform.html",{"data_list":mylist,"redirects":redirects,"id":id,"tab_name":tab_name})
        
        elif tab_name == "RentMachineryData":
            data = RentMachineryData.objects.filter(id = id).values()[0]
            mylist = RentMachineryData.DtypesMaterial()
            for i in range(len(mylist)):
                mydic = mylist[i]
                mydic["values"] = data[mydic["column"]]
            return render(request,"Mainpage/updateform.html",{"data_list":mylist,"redirects":redirects,"id":id,"tab_name":tab_name})
        
        elif tab_name == "TransportData":
            data = TransportData.objects.filter(id = id).values()[0]
            mylist = TransportData.DtypesMaterial()
            for i in range(len(mylist)):
                mydic = mylist[i]
                mydic["values"] = data[mydic["column"]]
                print(mylist[i])
            return render(request,"Mainpage/updateform.html",{"data_list":mylist,"redirects":redirects,"id":id,"tab_name":tab_name})
        
        elif tab_name == "LabourData":
            data = LabourData.objects.filter(id = id).values()[0]
            mylist = LabourData.DtypesMaterial()
            for i in range(len(mylist)):
                mydic = mylist[i]
                mydic["values"] = data[mydic["column"]]
            return render(request,"Mainpage/updateform.html",{"data_list":mylist,"redirects":redirects,"id":id,"tab_name":tab_name})
        
        elif tab_name == "LabourAttendance":
            data = LabourAttendance.objects.filter(id = id).values()[0]
            mylist = LabourAttendance.DtypesMaterial()
            for i in range(len(mylist)):
                mydic = mylist[i]
                mydic["values"] = data[mydic["column"]]
            return render(request,"Mainpage/updateform.html",{"data_list":mylist,"redirects":redirects,"id":id,"tab_name":tab_name})
        
        elif tab_name == "StockData":
            data = StockData.objects.filter(id = id).values()[0]
            mylist = StockData.DtypesMaterial()
            for i in range(len(mylist)):
                mydic = mylist[i]
                mydic["values"] = data[mydic["column"]]
            return render(request,"Mainpage/updateform.html",{"data_list":mylist,"redirects":redirects,"id":id,"tab_name":tab_name})
        
        elif tab_name == "IncomeData":
            data = IncomeData.objects.filter(id = id).values()[0]
            mylist = IncomeData.DtypesMaterial()
            for i in range(len(mylist)):
                mydic = mylist[i]
                mydic["values"] = data[mydic["column"]]
            return render(request,"Mainpage/updateform.html",{"data_list":mylist,"redirects":redirects,"id":id,"tab_name":tab_name})
        
        elif tab_name == "ExpenseData":
            data = ExpenseData.objects.filter(id = id).values()[0]
            mylist = ExpenseData.DtypesMaterial()
            for i in range(len(mylist)):
                mydic = mylist[i]
                mydic["values"] = data[mydic["column"]]
            return render(request,"Mainpage/updateform.html",{"data_list":mylist,"redirects":redirects,"id":id,"tab_name":tab_name})
        
        elif tab_name == "WorkProgreeData":
            data = WorkProgreeData.objects.filter(id = id).values()[0]
            mylist = WorkProgreeData.DtypesMaterial()
            for i in range(len(mylist)):
                mydic = mylist[i]
                mydic["values"] = data[mydic["column"]]
            return render(request,"Mainpage/updateform.html",{"data_list":mylist,"redirects":redirects,"id":id,"tab_name":tab_name})
        
        elif tab_name == "MachineryPurchaseData":
            data = MachineryPurchaseData.objects.filter(id = id).values()[0]
            mylist = MachineryPurchaseData.DtypesMaterial()
            for i in range(len(mylist)):
                mydic = mylist[i]
                mydic["values"] = data[mydic["column"]]
            return render(request,"Mainpage/updateform.html",{"data_list":mylist,"redirects":redirects,"id":id,"tab_name":tab_name})
        
    return render(request,"Mainpage/updateform.html")

def UpdateComplete(request):
    if request.method == "POST":
        id = request.POST.get("id")
        tab_name = request.POST.get("tab_name")
        redirects = request.POST.get("redirects")

        if tab_name == "MaterialsData":
            Date = request.POST.get("Date")
            manager_id = request.POST.get("manager_id")
            site_id = request.POST.get("site_id")
            Material_name = request.POST.get("Material_name")
            site_name = request.POST.get("site_name")
            work_details = request.POST.get("work_details")
            actual_qty = request.POST.get("actual_qty")
            Remarks = request.POST.get("Remarks")
            MaterialsData.objects.filter(id = id).update(Date = Date)
            MaterialsData.objects.filter(id = id).update(manager_id = manager_id)
            MaterialsData.objects.filter(id = id).update(site_id = site_id)
            MaterialsData.objects.filter(id = id).update(Material_name = Material_name)
            MaterialsData.objects.filter(id = id).update(site_name = site_name)
            MaterialsData.objects.filter(id = id).update(work_details = work_details)
            MaterialsData.objects.filter(id = id).update(actual_qty = actual_qty)
            MaterialsData.objects.filter(id = id).update(Remarks = Remarks)
            return redirect(redirects)
        
        elif tab_name == "RentMachineryData":
            data = RentMachineryData.objects.filter(id = id).values()[0]
            Date = request.POST.get("Date")
            manager_id = request.POST.get("manager_id")
            site_id = request.POST.get("site_id")
            site_name = request.POST.get("site_name")
            work_details = request.POST.get("work_details")
            machinery_name = request.POST.get("machinery_name")
            days = request.POST.get("days")
            Amount = request.POST.get("Amount")
            RentMachineryData.objects.filter(id = id).update(Date = Date)
            RentMachineryData.objects.filter(id = id).update(manager_id = manager_id)
            RentMachineryData.objects.filter(id = id).update(site_id = site_id)
            RentMachineryData.objects.filter(id = id).update(machinery_name = machinery_name)
            RentMachineryData.objects.filter(id = id).update(site_name = site_name)
            RentMachineryData.objects.filter(id = id).update(work_details = work_details)
            RentMachineryData.objects.filter(id = id).update(days = days)
            RentMachineryData.objects.filter(id = id).update(Amount = Amount)
            return redirect(redirects)

        elif tab_name == "TransportData":
            data = TransportData.objects.filter(id = id).values()[0]
            Date = request.POST.get("Date")
            manager_id = request.POST.get("manager_id")
            site_id = request.POST.get("site_id")
            site_name = request.POST.get("site_name")
            Material_name = request.POST.get("Material_name")
            vehical_number = request.POST.get("vehical_number")
            kilometer = request.POST.get("kilometer")
            Amount = request.POST.get("Amount")
            Deliver_from = request.POST.get("Deliver_from")
            Deliver_To = request.POST.get("Deliver_To")
            TransportData.objects.filter(id = id).update(Date = Date)
            TransportData.objects.filter(id = id).update(manager_id = manager_id)
            TransportData.objects.filter(id = id).update(site_id = site_id)
            TransportData.objects.filter(id = id).update(vehical_number = vehical_number)
            TransportData.objects.filter(id = id).update(site_name = site_name)
            TransportData.objects.filter(id = id).update(Material_name = Material_name)
            TransportData.objects.filter(id = id).update(kilometer = kilometer)
            TransportData.objects.filter(id = id).update(Amount = Amount)
            TransportData.objects.filter(id = id).update(Deliver_from = Deliver_from)
            TransportData.objects.filter(id = id).update(Deliver_To = Deliver_To)
            return redirect(redirects)

        elif tab_name == "LabourData":
            data = LabourData.objects.filter(id = id).values()[0]
            manager_id = request.POST.get("manager_id")
            labour_name = request.POST.get("labour_name")
            site_id = request.POST.get("site_id")
            site_name = request.POST.get("site_name")
            labour_age = request.POST.get("labour_age")
            labour_gender = request.POST.get("labour_gender")
            salary = request.POST.get("salary")
            work_details = request.POST.get("work_details")
            LabourData.objects.filter(id = id).update(manager_id = manager_id)
            LabourData.objects.filter(id = id).update(labour_name = labour_name)
            LabourData.objects.filter(id = id).update(site_id = site_id)
            LabourData.objects.filter(id = id).update(site_name = site_name)
            LabourData.objects.filter(id = id).update(labour_age = labour_age)
            LabourData.objects.filter(id = id).update(labour_gender = labour_gender)
            LabourData.objects.filter(id = id).update(salary = salary)
            LabourData.objects.filter(id = id).update(work_details = work_details)
            return redirect(redirects)

        elif tab_name == "LabourAttendance":
            data = LabourAttendance.objects.filter(id = id).values()[0]
            manager_id = request.POST.get("manager_id")
            Date = request.POST.get("Date")
            site_id = request.POST.get("site_id")
            site_name = request.POST.get("site_name")
            work_details = request.POST.get("work_details")
            labour_id = request.POST.get("labour_id")
            labour_name = request.POST.get("labour_name")
            LabourAttendance.objects.filter(id = id).update(manager_id = manager_id)
            LabourAttendance.objects.filter(id = id).update(Date = Date)
            LabourAttendance.objects.filter(id = id).update(site_id = site_id)
            LabourAttendance.objects.filter(id = id).update(site_name = site_name)
            LabourAttendance.objects.filter(id = id).update(work_details = work_details)
            LabourAttendance.objects.filter(id = id).update(labour_id = labour_id)
            LabourAttendance.objects.filter(id = id).update(labour_name = labour_name)
            return redirect(redirects)


        elif tab_name == "StockData":
            data = StockData.objects.filter(id = id).values()[0]
            manager_id = request.POST.get("manager_id")
            site_id = request.POST.get("site_id")
            site_name = request.POST.get("site_name")
            actual_qty = request.POST.get("actual_qty")
            Material_name = request.POST.get("Material_name")
            StockData.objects.filter(id = id).update(manager_id = manager_id)
            StockData.objects.filter(id = id).update(site_id = site_id)
            StockData.objects.filter(id = id).update(site_name = site_name)
            StockData.objects.filter(id = id).update(actual_qty = actual_qty)
            StockData.objects.filter(id = id).update(Material_name = Material_name)
            return redirect(redirects)


        elif tab_name == "IncomeData":
            data = IncomeData.objects.filter(id = id).values()[0]
            manager_id = request.POST.get("manager_id")
            Date = request.POST.get("Date")
            Time = request.POST.get("Time")
            payment_mode = request.POST.get("payment_mode")
            payee_name = request.POST.get("payee_name")
            Amount = request.POST.get("Amount")
            Remark = request.POST.get("Remark")
            IncomeData.objects.filter(id = id).update(manager_id = manager_id)
            IncomeData.objects.filter(id = id).update(Date = Date)
            IncomeData.objects.filter(id = id).update(Time = Time)
            IncomeData.objects.filter(id = id).update(payment_mode = payment_mode)
            IncomeData.objects.filter(id = id).update(payee_name = payee_name)
            IncomeData.objects.filter(id = id).update(Amount = Amount)
            IncomeData.objects.filter(id = id).update(Remark = Remark)
            return redirect(redirects)

        elif tab_name == "ExpenseData":
            data = ExpenseData.objects.filter(id = id).values()[0]
            manager_id = request.POST.get("manager_id")
            Date = request.POST.get("Date")
            Time = request.POST.get("Time")
            payment_mode = request.POST.get("payment_mode")
            payee_name = request.POST.get("payee_name")
            Amount = request.POST.get("Amount")
            Remark = request.POST.get("Remark")
            ExpenseData.objects.filter(id = id).update(manager_id = manager_id)
            ExpenseData.objects.filter(id = id).update(Date = Date)
            ExpenseData.objects.filter(id = id).update(Time = Time)
            ExpenseData.objects.filter(id = id).update(payment_mode = payment_mode)
            ExpenseData.objects.filter(id = id).update(payee_name = payee_name)
            ExpenseData.objects.filter(id = id).update(Amount = Amount)
            ExpenseData.objects.filter(id = id).update(Remark = Remark)
            return redirect(redirects)
        
        elif tab_name == "WorkProgreeData":
            data = WorkProgreeData.objects.filter(id = id).values()[0]
            manager_id = request.POST.get("manager_id")
            Date = request.POST.get("Date")
            site_id = request.POST.get("site_id")
            site_name = request.POST.get("site_name")
            work_details = request.POST.get("work_details")
            labour_id = request.POST.get("labour_id")
            labour_name = request.POST.get("labour_name")
            Work_progress = request.POST.get("Work_progress")
            Remark = request.POST.get("Remark")
            WorkProgreeData.objects.filter(id = id).update(manager_id = manager_id)
            WorkProgreeData.objects.filter(id = id).update(Date = Date)
            WorkProgreeData.objects.filter(id = id).update(site_id = site_id)
            WorkProgreeData.objects.filter(id = id).update(site_name = site_name)
            WorkProgreeData.objects.filter(id = id).update(work_details = work_details)
            WorkProgreeData.objects.filter(id = id).update(labour_id = labour_id)
            WorkProgreeData.objects.filter(id = id).update(labour_name = labour_name)
            WorkProgreeData.objects.filter(id = id).update(Work_progress = Work_progress)
            WorkProgreeData.objects.filter(id = id).update(Remark = Remark)
            return redirect(redirects)

        elif tab_name == "MachineryPurchaseData":
            data = MachineryPurchaseData.objects.filter(id = id).values()[0]
            manager_id = request.POST.get("manager_id")
            Date = request.POST.get("Date")
            site_id = request.POST.get("site_id")
            site_name = request.POST.get("site_name")
            machinery_name = request.POST.get("machinery_name")
            Rate = request.POST.get("Rate")
            Remark = request.POST.get("Remark")
            MachineryPurchaseData.objects.filter(id = id).update(manager_id = manager_id)
            MachineryPurchaseData.objects.filter(id = id).update(Date = Date)
            MachineryPurchaseData.objects.filter(id = id).update(site_id = site_id)
            MachineryPurchaseData.objects.filter(id = id).update(site_name = site_name)
            MachineryPurchaseData.objects.filter(id = id).update(machinery_name = machinery_name)
            MachineryPurchaseData.objects.filter(id = id).update(Rate = Rate)
            MachineryPurchaseData.objects.filter(id = id).update(Remark = Remark)
            return redirect(redirects)
    return redirect('/dashboard/')

def Details(request):
    if request.method == "POST":
        id = request.POST.get("id")
        tab_name = request.POST.get("tab_name")
        if tab_name == "MaterialsData":
            data = MaterialsData.objects.filter(id = id).values()[0]
            main_list = []
            for i in data:
                mydic = {}
                mydic["id"] = i
                mydic["value"] = data[i]
                main_list.append(mydic)
            return render(request,"Mainpage/details.html",{"data":main_list})
        
        elif tab_name == "RentMachineryData":
            data = RentMachineryData.objects.filter(id = id).values()[0]
            main_list = []
            for i in data:
                mydic = {}
                mydic["id"] = i
                mydic["value"] = data[i]
                main_list.append(mydic)
            return render(request,"Mainpage/details.html",{"data":main_list})
        
        elif tab_name == "TransportData":
            data = TransportData.objects.filter(id = id).values()[0]
            main_list = []
            for i in data:
                mydic = {}
                mydic["id"] = i
                mydic["value"] = data[i]
                main_list.append(mydic)
            return render(request,"Mainpage/details.html",{"data":main_list})  
              
        elif tab_name == "LabourData":
            data = LabourData.objects.filter(id = id).values()[0]
            main_list = []
            for i in data:
                mydic = {}
                mydic["id"] = i
                mydic["value"] = data[i]
                main_list.append(mydic)
            return render(request,"Mainpage/details.html",{"data":main_list})
        
        elif tab_name == "LabourAttendance":
            data = LabourAttendance.objects.filter(id = id).values()[0]
            main_list = []
            for i in data:
                mydic = {}
                mydic["id"] = i
                mydic["value"] = data[i]
                main_list.append(mydic)
            return render(request,"Mainpage/details.html",{"data":main_list})
        
        elif tab_name == "StockData":
            data = StockData.objects.filter(id = id).values()[0]
            main_list = []
            for i in data:
                mydic = {}
                mydic["id"] = i
                mydic["value"] = data[i]
                main_list.append(mydic)
            return render(request,"Mainpage/details.html",{"data":main_list})
        
        elif tab_name == "IncomeData":
            data = IncomeData.objects.filter(id = id).values()[0]
            main_list = []
            for i in data:
                mydic = {}
                mydic["id"] = i
                mydic["value"] = data[i]
                main_list.append(mydic)
            return render(request,"Mainpage/details.html",{"data":main_list})
        
        elif tab_name == "ExpenseData":
            data = ExpenseData.objects.filter(id = id).values()[0]
            main_list = []
            for i in data:
                mydic = {}
                mydic["id"] = i
                mydic["value"] = data[i]
                main_list.append(mydic)
            return render(request,"Mainpage/details.html",{"data":main_list})
        
        elif tab_name == "WorkProgreeData":
            data = WorkProgreeData.objects.filter(id = id).values()[0]
            main_list = []
            for i in data:
                mydic = {}
                mydic["id"] = i
                mydic["value"] = data[i]
                main_list.append(mydic)
            return render(request,"Mainpage/details.html",{"data":main_list})
        
        elif tab_name == "MachineryPurchaseData":
            data = MachineryPurchaseData.objects.filter(id = id).values()[0]
            main_list = []
            for i in data:
                mydic = {}
                mydic["id"] = i
                mydic["value"] = data[i]
                main_list.append(mydic)
            return render(request,"Mainpage/details.html",{"data":main_list})
        
    return render(request,"Mainpage/details.html")

def ManageSearch(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST.get("data")
            if(len(SiteData.objects.filter(site_name__contains=data).values())>0):
                return redirect('/sites/')
            else:
                messages.warning(request,"Not Found")
                return redirect("/")
        return redirect("/")
    else:
        messages.warning(request,"Please first complete the login!!")
        return redirect("/")

def Logout(request):
    logout(request)
    return redirect("/")