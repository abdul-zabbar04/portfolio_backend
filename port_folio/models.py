from django.db import models

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=100)
    image= models.URLField(max_length=300)
    features= models.TextField(max_length=500)
    description= models.TextField(max_length=800, null=True, blank=True)
    used_technology= models.CharField(max_length=400)
    github_frontend= models.URLField(max_length=300, null=True, blank=True)
    github_link_backend= models.URLField(max_length=300, null=True, blank=True)
    live_frontend= models.URLField(max_length=300, null=True, blank=True)
    live_backend= models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name= models.CharField(max_length=30)
    email= models.EmailField(max_length=40)
    phone= models.CharField(max_length=15)
    message= models.TextField(max_length=300)
    def __str__(self):
        return self.name
    
class Academic(models.Model):
    CURRENT=(
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing'),
        )
    institution= models.CharField(max_length=150)
    degree= models.CharField(max_length=50)
    years= models.CharField(max_length=15)
    gpa= models.CharField(max_length=15)
    current= models.CharField(max_length=10, choices=CURRENT)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True) 
    def __str__(self):
        return self.degree
    class Meta:
        ordering = ['-created_at']

class Skill(models.Model):
    DISPLAYED_IN= (
        ("1", "1st"),
        ("2", "2nd"),
        ("3", "3rd"),
        ("4", "4th"),
        ("5", "5th"),
        )
    displayed_in= models.CharField(max_length=10, choices=DISPLAYED_IN, unique=True)
    category= models.CharField(max_length=50)
    icon= models.CharField(max_length=20)
    items= models.CharField(max_length=250)
    def __str__(self):
        return self.category
    class Meta:
        ordering = ['displayed_in']