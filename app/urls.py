from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import AuthorApi, ArticleApi, CommentApi, CategoryApi

urlpatterns = [
    path('authors/', AuthorApi.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorApi.as_view(), name='author-detail'),
    
    path('articles/', ArticleApi.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleApi.as_view(), name='article-detail'),
    
    path('comments/', CommentApi.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentApi.as_view(), name='comment-detail'),
    
    path('categories/', CategoryApi.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryApi.as_view(), name='category-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
