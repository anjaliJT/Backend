from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    billing_cycle = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plans"

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company_name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name
    
class Subscription(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    current_period_start = models.DateField()
    current_period_end = models.DateField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('cancelled', 'Cancelled')])
    cancelled_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        return f"{self.customer.name} - {self.plan.name}"
    
class Invoice(models.Model):
    subscription_id = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    due_date = models.DateField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self):
        return f"Invoice for {self.subscription.customer.name} - {self.subscription.plan.name}"
    

class PaymentAttempt(models.Model):
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=[('success', 'Success'), ('failed', 'Failed')])
    provider_reference = models.CharField(max_length=100)
    failure_reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Payment Attempt"
        verbose_name_plural = "Payment Attempts"

    def __str__(self):
        return f"Payment Attempt for {self.invoice.subscription.customer.name} - {self.invoice.subscription.plan.name}"
    
class LedgerEntry(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    entry_type = models.CharField(max_length=20)  # e.g., 'debit' or 'credit'
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    reference_id = models.CharField(max_length=100)  # e.g., payment attempt ID or invoice ID
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ledger Entry"
        verbose_name_plural = "Ledger Entries"

    def __str__(self):
        return f"Ledger Entry for {self.customer.name} - {self.invoice.subscription.plan.name}"