from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer
from .models import Comment

# Create your views here.
class CommentAPIView(APIView):
    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        return Response(serializer.data)

class PostCommentView(APIView):
    def get(self,_, pk=None):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments ,many=True)
        return Response(serializer.data)
        

