from django.contrib import admin
from .models import Drug, Prescription, Transaction, Client, Branch

@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'generic_name', 'batch', 'release_date', 'expiry_date', 'quantity', 'pharmacy_branches')

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('doctor_full_name', 'drug', 'prescription_number', 'quantity_in_stock', 'pharmacy_branches')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('pharmacist_name', 'doctor_name', 'client_name', 'drug', 'transaction_date')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_full_name', 'drug', 'dispense_date')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('pharmacy_name', 'address', 'operating_hours', 'phone_number', 'drug')
