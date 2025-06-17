from django.contrib import admin,messages
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .  import models
from django.db.models import Count

# Register your models here.
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ['title', 'collection']
#     list_filter = ['collection']
#     search_fields = ['title', 'collection__name']
        
    
# admin.site.register(models.News)

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'collection','collection_count']
    list_filter = ['title','collection','created_at','updated_at']
    list_editable = ['collection']
    search_fields = ['title', 'collection__name']
    ordering = ['title']
    # if foreingkey item is used then it will reduce the query count
    list_select_related = ['collection']
    list_per_page = 10

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(collection_news_count=Count('collection__news'))

    @admin.display(ordering='collection', description='Collection Count')
    def collection_count(self, obj):
        return obj.collection_news_count if obj.collection_news_count else 0
    
 
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_news']

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'updated_at']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'news', 'content', 'created_at', 'updated_at']

@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['news', 'user', 'created_at', 'vote_count']

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(vote_count=Count('news__votes'))

    @admin.display(ordering='news', description='Vote Count')
    def vote_count(self, obj):
        return obj.news.votes.count()
    
