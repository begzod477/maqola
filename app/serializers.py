from rest_framework import serializers
from .models import Author, Article, Comment, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'pub_date', 'author']

    def create(self, validated_data):
        author_data = validated_data.pop('author', None)
        if author_data:
            author = Author.objects.create(**author_data)
            validated_data['author'] = author
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        if author_data:
            instance.author.name = author_data.get('name', instance.author.name)
            instance.author.save()
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'email', 'comment_text']

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
    class Meta:
        model = Category
        fields = ['id', 'name']
