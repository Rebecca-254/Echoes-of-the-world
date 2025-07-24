from django.urls import path
from .views import HomePageView
from . import views

app_name = 'news'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('tag/<slug:slug>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('articles/<slug:slug>/comment/', views.CommentCreateView.as_view(), name='add_comment'),
    path('articles/<slug:slug>/react/', views.ReactionView.as_view(), name='react'),
    path('newsletter/subscribe/', views.NewsletterSubscribeView.as_view(), name='newsletter_subscribe'),
]