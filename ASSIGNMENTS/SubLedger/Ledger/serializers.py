from rest_framework import serializers
from models import Plan, Customer, Subscription, Invoice, PaymentAttempt

class planSerializer(serializers.ModelSerializer): 
    class Meta:
        plan = Plan
        fields = ['id','account_n']

class customerSerializer(serializers.ModelSerializer):
    class meta: 
        customer = Customer
        fields = []
    
class subscriptionSerializer(serializers.ModelSerializer):
    class meta: 
        customer = Customer
        fields = []
    
class invoiceSerializer(serializers.ModelSerializer):
    class meta: 
        customer = Customer
        fields = []
    
class customerSerializer(serializers.ModelSerializer):
    class meta: 
        customer = Customer
        fields = []
    

