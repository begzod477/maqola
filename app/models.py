from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=35)
    comment_text = models.TextField()
    comment_add_date = models.DateField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.username

