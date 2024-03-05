""" from django.shortcuts import render
from Pharmacy.models import Medicine


def news_home(request):
    return render(request, 'main/about.html')
def Medicine(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharmacy/medicine_list.html', {'medicines': medicines})
 """



from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('', views.news_home, name='news_home'),
    path('Medicine/<int:drug_id>/', views.drug_detail, name='drug_detail'),
    path('Prescription/<int:prescription_id>/', views.prescription_detail, name='prescription_detail'),
    path('Transaction/<int:transaction_id>/', views.transaction_detail, name='transaction_detail'),
    path('Client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('Branch/<int:branch_id>/', views.branch_detail, name='branch_detail'),
]
