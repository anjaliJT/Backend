from django.db import models

# Create your models here.
class KBEntry(models.Model):
    class Category(models.TextChoices): 
        API = 'API',"API"
        DATABASE = 'database', 'Database'
        CLOUD = 'cloud','Cloud'
        FRAMEWORK = 'framework',"Framework"
        AI = 'AI','AI'
        GENERAL = 'general', "General"

    questions = models.TextField()
    answer = models.TextField() 
    category =moels.CharField(max_length=20,choices=Category.choices)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self): 
        return self.queston[:80]