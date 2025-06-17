from rest_framework import serializers
from news.models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model= News
        fields=['title','content','image','collection','created_at']

    
    # def isNew(self,news:News):
    #     if news.created_at

