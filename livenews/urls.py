from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView
from .import views


urlpatterns = [
    #path('', views.home, name='news-home'),
    path('', NewsListView.as_view(), name='news-home'),
    path('post/<int:pk>/', NewsDetailView.as_view(), name='post-detail'),
    path('post/new/', NewsCreateView.as_view(), name='post-create'),
    path('about/', views.about, name="news-about"),
]
