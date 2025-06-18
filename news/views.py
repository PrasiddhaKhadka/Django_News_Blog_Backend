from news.serializers import NewsSerializer
from .models import News
from rest_framework.response import Response;
from rest_framework.decorators import api_view 
from django.shortcuts import get_object_or_404
from rest_framework import status




# Create your views here.
@api_view(['GET','POST'])
def news_list(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET','PUT','DELETE'])
def news_detail(request, pk):
    # news_detail = News.objects.get(pk=pk)
    if request.method == 'GET':
        news_detail = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(news_detail, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        news_detail = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(news_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'News has been updated successfully',
                'data': serializer.data
            },status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        news_detail = get_object_or_404(News, pk=pk)
        news_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)