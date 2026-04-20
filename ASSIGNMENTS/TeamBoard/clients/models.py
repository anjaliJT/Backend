from django.db import models
from django.contrib.auth.models import user

# Create your models here.
class Company(models.Model):
    class Role(models.TextChoices): 
        ADMIN = 'admin', 'Admin'
        CLIENT = 'client', "Client"

    user = models.OneToOneField(
        User, 
        one_delete=models.CASCADE,
        related_name='company'
    )
    company_name = modelsf.CharField(max_length=255)
    api_key = models.CharField(max_length=64, unique=True, blank=True)
    role = models.CharField(max_length=10,choices=Role.choices,default=Role.CLIENT)
    created_at = models.DateTimeField(auto_now_add=True)


class QueryLog(models.Model):
    company       = models.ForeignKey(
                        Company,
                        on_delete=models.CASCADE,
                        related_name='query_logs'
                    )
    search_term   = models.CharField(max_length=255)
    results_count = models.IntegerField()  # how many KB entries matched
    queried_at    = models.DateTimeField(auto_now_add=True)
