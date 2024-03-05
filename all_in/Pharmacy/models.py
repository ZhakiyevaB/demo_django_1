from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=128)
    generic_name = models.CharField(max_length=128)
    batch = models.CharField(max_length=128)
    release_date = models.DateField()
    expiry_date = models.DateField()
    quantity = models.IntegerField()
    pharmacy_branches = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    doctor_full_name = models.CharField(max_length=128)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='prescriptions')
    prescription_number = models.CharField(max_length=128)
    quantity_in_stock = models.IntegerField()
    pharmacy_branches = models.CharField(max_length=128)

    def __str__(self):
        return self.prescription_number

class Transaction(models.Model):
    pharmacist_name = models.CharField(max_length=128)
    doctor_name = models.CharField(max_length=128)
    client_name = models.CharField(max_length=128)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='transactions')
    transaction_date = models.DateField()

    def __str__(self):
        return self.pharmacist_name

class Client(models.Model):
    client_full_name = models.CharField(max_length=128)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='clients', null=True)
    dispense_date = models.DateField(null=True)

    def __str__(self):
        return self.client_full_name

class Branch(models.Model):
    pharmacy_name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    operating_hours = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='branches', null=True)

    def __str__(self):
        return self.pharmacy_name


