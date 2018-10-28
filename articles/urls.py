from django.urls import path

from .views import ArticleListView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView, ArticleCreateView, add_comment_to_article

urlpatterns = [
    path('<int:pk>/comment/', add_comment_to_article, name='add_comment_to_article'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name="article_new"),
    path('', ArticleListView.as_view(), name='article_list'),
]
