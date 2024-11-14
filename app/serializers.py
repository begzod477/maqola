from rest_framework import serializers
from .models import Author, Article, Comment, Category

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    pub_date = serializers.DateField()
    author = AuthorSerializer(read_only=True)

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = AuthorSerializer().create(author_data)
        return Article.objects.create(author=author, **validated_data)
    
    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        if author_data:
            author = AuthorSerializer().update(instance.author, author_data)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    comment_text = serializers.CharField()

    def create(self, validated_data):
        article_id = validated_data.pop('article_id')
        article = Article.objects.get(id=article_id)
        return Comment.objects.create(article=article, **validated_data)
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.comment_text = validated_data.get('comment_text', instance.comment_text)
        instance.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    