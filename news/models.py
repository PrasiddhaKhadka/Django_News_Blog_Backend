from django.db import models

# Create your models here.
class Collection(models.Model):
    title= models.CharField(max_length=255)
    featured_news= models.ForeignKey('News', on_delete=models.SET_NULL,null=True, related_name= "+")

class News(models.Model):
    title= models.CharField(max_length=255)
    content= models.TextField()
    image= models.ImageField(upload_to='images/', null=True, blank=True)
    collection= models.ForeignKey('Collection', on_delete=models.PROTECT)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


class Vote(models.Model):
    news= models.ForeignKey('News', on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    news= models.ForeignKey('News', on_delete=models.CASCADE)
    content= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)



    

    