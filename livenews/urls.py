from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView, PostNewsListView
from .import views


urlpatterns = [
    
    path('', NewsListView.as_view(), name='news-home'),
    path('user/<str:username>', PostNewsListView.as_view(), name='user-news'),
    path('post/<int:pk>/', NewsDetailView.as_view(), name='post-detail'),
    path('post/new/', NewsCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', NewsUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', NewsDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name="news-about"),
]
