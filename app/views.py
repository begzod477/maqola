from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Category, Comment, Article, Author

# Create your views here.

class IndexApiView(APIView):
    def get(self, request: Request):
        articles = Article.objects.all()
        comments = Comment.objects.all()
        categories = Category.objects.all()
        authors = Author.objects.all()

        new_authors = []
        for author in authors:
            new_authors.append({
                "id": author.id,
                "name": author.name,
                "age": author.age,
                "photo": author.photo.url if author.photo else None  
            })

        new_categories = []
        for category in categories:
            new_categories.append({
                "id": category.id,
                "name": category.name,
                "photo": category.photo.url if category.photo else None  
            })

        new_comments = []
        for comment in comments:
            new_comments.append({
                "id": comment.id,
                "username": comment.username,
                "email": comment.email,
                "comment_text": comment.comment_text,
                "comment_add_date": comment.comment_add_date,
                "photo": comment.photo.url if comment.photo else None  
            })

        new_articles = []
        for article in articles:
            new_articles.append({
                "id": article.id,
                "title": article.title,
                "pub_date": article.pub_date,
                "category": article.category.name,
                "author": article.author.name  if article.author else None,  
                "photo": article.photo.url if article.photo else None  
            })

        return Response({
            "message": "welcome whatsapp",
            "articles": new_articles,
            "comments": new_comments,
            "categories": new_categories,
            "authors": new_authors
        })
