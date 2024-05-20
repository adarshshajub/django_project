from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tree(models.Model):
    id =  models.AutoField(primary_key=True, editable=False, auto_created = True, serialize = False)
    tree_name = models.TextField(max_length=100)
    tree_scientific_name = models.TextField(max_length=200)
    tree_description = models.TextField(max_length=10000)
    created_by = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE, editable=False)
    search_link_key = models.TextField(max_length=200)

    def __str__(self):
        return f"| {self.tree_name } | { self.tree_scientific_name } | {self.tree_description} | { self.created_by } | {self.search_link_key}"
    
    