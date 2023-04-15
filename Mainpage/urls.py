from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homepage,name="Homepage"),
    path('dashboard/',views.DashboardPage,name="DashboardPage"),
    path('login/',views.Loginsystem,name="Loginsystem"),
    path('sites/',views.SitesPage,name="SitesPage"),
    path('materials/',views.ManageMaterial,name="ManageMaterial"),
    path('manage-machines/',views.ManageMachine,name="ManageMachine"),
    path('transport/',views.ManageTransport,name="ManageTransport"),
    path('labour/',views.ManageLabour,name="ManageLabour"),
    path('godown/',views.ManageGodownStocks,name="ManageGodownStocks"),
    path('accounting/',views.ManageAccounting,name="ManageAccounting"),
    path('work-progress/',views.ManageProgress,name="ManageProgress"),
    path('attendance/',views.ManageAttendance,name="ManageAttendance"),
    path('purchase-machine/',views.ManageMachinery,name="ManageMachinery"),
    path('reports/',views.ManageReports,name="ManageReports"),
    path('profit/',views.ManageProfit,name="ManageProfit"),
    path('expense/',views.ManageExpenses,name="ManageExpenses"),
    path('contact/',views.ContactManager,name="ContactManager"),
    path('Delete-Manager/',views.DeleteManager,name="DeleteManager"),
    path('update-form/',views.UpdateData,name="UpdateData"),
    path('update-complete/',views.UpdateComplete,name="UpdateComplete"),
    path('details/',views.Details,name="Details"),
    path('search/',views.ManageSearch,name="ManageSearch"),
    path('logout/',views.Logout,name="Logout"),
]