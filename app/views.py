from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Category, Comment, Article, Author
from .serializers import AuthorSerializer,ArticleSerializer, CommentSerializer, CategorySerializer


# Create your views here.

class AuthorApi(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                author = Author.objects.get(pk=pk)
                serializer = AuthorSerializer(author)
                return Response(serializer.data)
            except:
                return Response({'error': 'Author not found'}, status=404)
        authors = Author.objects.all()
        return Response(AuthorSerializer(authors,).data)
    
    def post(self, request: Request, pk=None):
        if pk:
            return Response({'error': 'Not allowed to create author with an existing id'}, status=404)
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = serializer.save()
        return Response(AuthorSerializer(author).data)
    
    def put(self, request: Request, pk):
        if pk:
            try:
                author = Author.objects.get(pk=pk)
                serializer = AuthorSerializer(author, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(AuthorSerializer(author).data)
            except:
                return Response({'error': 'Author not found'}, status=404)
        
        return Response({'error': 'Author id is required for this operation'}, status=404)


    def delete(self, request: Request, pk=None):
        if pk:
            try:
                author = Author.objects.get(pk=pk)
                author.delete()
                return Response({'message': 'Author deleted successfully'})
            except:
                return Response({'error': 'Author not found'}, status=404)
        
        return Response({'error': 'Author id is required for this operation'}, status=404)
        

class ArticleApi(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                article = Article.objects.get(pk=pk)
                serializer = ArticleSerializer(article)
                return Response(serializer.data)
            except:
                return Response({'error': 'Article not found'}, status=404)
        articles = Article.objects.all()
        return Response(ArticleSerializer(articles,).data)
    
    def post(self, request: Request, pk=None):
        if pk:
            return Response({'error': 'Not allowed to create article with an existing id'}, status=404)
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return Response(ArticleSerializer(article).data)
    
    def put(self, request: Request, pk):
        if pk:
            try:
                article = Article.objects.get(pk=pk)
                serializer = ArticleSerializer(article, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(ArticleSerializer(article).data)
            except:
                return Response({'error': 'Article not found'}, status=404)
        
        return Response({'error': 'Article id is required for this operation'}, status=404)
    
    def delete(self, request: Request, pk=None):
        if pk:
            try:
                article = Article.objects.get(pk=pk)
                article.delete()
                return Response({'message': 'Article deleted successfully'})
            except:
                return Response({'error': 'Article not found'}, status=404)
        
        return Response({'error': 'Article id is required for this operation'}, status=404)
    


class CommentApi(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                comment = Comment.objects.get(pk=pk)
                serializer = CommentSerializer(comment)
                return Response(serializer.data)
            except:
                return Response({'error': 'Comment not found'}, status=404)
        comments = Comment.objects.all()
        return Response(CommentSerializer(comments,).data)
    
    def post(self, request: Request, pk=None):
        if pk:
            return Response({'error': 'Not allowed to create comment with an existing id'}, status=404)
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response(CommentSerializer(comment).data)
    
    def put(self, request: Request, pk):
        if pk:
            try:
                comment = Comment.objects.get(pk=pk)
                serializer = CommentSerializer(comment, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(CommentSerializer(comment).data)
            except:
                return Response({'error': 'Comment not found'}, status=404)
        
        return Response({'error': 'Comment id is required for this operation'}, status=404)
    
    def delete(self, request: Request, pk=None):
        if pk:
            try:
                comment = Comment.objects.get(pk=pk)
                comment.delete()
                return Response({'message': 'Comment deleted successfully'})
            except:
                return Response({'error': 'Comment not found'}, status=404)
        
        return Response({'error': 'Comment id is required for this operation'}, status=404)
    

class CategoryApi(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category)
                return Response(serializer.data)
            except:
                return Response({'error': 'Category not found'}, status=404)
        categories = Category.objects.all()
        return Response(CategorySerializer(categories,).data)
    
    def post(self, request: Request, pk=None):
        if pk:
            return Response({'error': 'Not allowed to create category with an existing id'}, status=404)
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.save()
        return Response(CategorySerializer(category).data)
    
    def put(self, request: Request, pk):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(CategorySerializer(category).data)
            except:
                return Response({'error': 'Category not found'}, status=404)
        
        return Response({'error': 'Category id is required for this operation'}, status=404)
    
    def delete(self, request: Request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                category.delete()
                return Response({'message': 'Category deleted successfully'})
            except:
                return Response({'error': 'Category not found'}, status=404)
        
        return Response({'error': 'Category id is required for this operation'}, status=404)



            










































    # def get(self, request: Request):
    #     articles = Article.objects.all()
    #     comments = Comment.objects.all()
    #     categories = Category.objects.all()
    #     authors = Author.objects.all()

    #     new_authors = []
    #     for author in authors:
    #         new_authors.append({
    #             "id": author.id,
    #             "name": author.name,
    #             "age": author.age,
    #             "photo": author.photo.url if author.photo else None  
    #         })

    #     new_categories = []
    #     for category in categories:
    #         new_categories.append({
    #             "id": category.id,
    #             "name": category.name,
    #             "photo": category.photo.url if category.photo else None  
    #         })

    #     new_comments = []
    #     for comment in comments:
    #         new_comments.append({
    #             "id": comment.id,
    #             "username": comment.username,
    #             "email": comment.email,
    #             "comment_text": comment.comment_text,
    #             "comment_add_date": comment.comment_add_date,
    #             "photo": comment.photo.url if comment.photo else None  
    #         })

    #     new_articles = []
    #     for article in articles:
    #         new_articles.append({
    #             "id": article.id,
    #             "title": article.title,
    #             "pub_date": article.pub_date,
    #             "category": article.category.name,
    #             "author": article.author.name  if article.author else None,  
    #             "photo": article.photo.url if article.photo else None  
    #         })

    #     return Response({
    #         "message": "welcome whatsapp",
    #         "articles": new_articles,
    #         "comments": new_comments,
    #         "categories": new_categories,
    #         "authors": new_authors
    #     })
