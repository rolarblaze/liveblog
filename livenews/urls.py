from django.urls import path
from .views import NewsListView, NewsDetailView
from .import views


urlpatterns = [
    #path('', views.home, name='news-home'),
    path('', NewsListView.as_view(), name='news-home'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('about/', views.about, name="news-about"),
]
