

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from news.models import Article, Category
from django.db.models import Count, Q
from django.views import View
from django.contrib import messages

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get latest articles
        context['featured_articles'] = Article.objects.filter(
            is_published=True, 
            is_featured=True
        ).select_related('author', 'category').order_by('-created_at')[:3]
        
        context['latest_articles'] = Article.objects.filter(
            is_published=True
        ).select_related('author', 'category').order_by('-created_at')[:6]
        
        # Category sections for homepage
        category_sections = {}
        categories = Category.objects.all()
        for category in categories:
            articles = Article.objects.filter(
                is_published=True,
                category=category
            ).select_related('author', 'category').order_by('-created_at')[:4]
            if articles.exists():
                category_sections[category] = articles
        context['category_sections'] = category_sections
        
        # Get categories with article count
        context['categories'] = Category.objects.annotate(
            article_count=Count('article', filter=Q(article__is_published=True))
        )
        
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ContactView(TemplateView):
    template_name = 'core/contact.html'
    
    def post(self, request, *args, **kwargs):
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Here you would typically send an email or save to database
        # For now, just show a success message
        
        messages.success(request, 'Thank you for your message. We will get back to you soon!')
        
        return self.get(request, *args, **kwargs)