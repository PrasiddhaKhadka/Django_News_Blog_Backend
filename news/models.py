from django.db import models

# Create your models here.
class Collection(models.Model):
    title= models.CharField(max_length=255)
    featured_news= models.ForeignKey('News', on_delete=models.SET_NULL,null=True, related_name= "+")

    def __str__(self):
        return self.title

class News(models.Model):
    title= models.CharField(max_length=255)
    content= models.TextField()
    image= models.ImageField(upload_to='images/', null=True, blank=True)
    collection= models.ForeignKey(Collection, on_delete=models.PROTECT)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']


class User(models.Model):
    name= models.CharField(max_length=255)
    email= models.EmailField(unique=True)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Vote(models.Model):
    news= models.ForeignKey(News, on_delete=models.CASCADE, related_name= "votes")
    # user can vote in multiple post -> many votes can be related to one user (many to one)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name= "vote",null=True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['news', 'user'], name='unique_vote_per_user')
        ]

class Comment(models.Model):
    # many comments can be related to one user
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name= "comment",null=True,blank=True)
    news= models.ForeignKey(News, on_delete=models.CASCADE)
    content= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)





    

    