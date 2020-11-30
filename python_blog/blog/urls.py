from django.urls import path

from blog import views
from blog.views import PostListView, \
    PostDetailView, \
    PostCreateView, \
    PostUpdateView, \
    PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='home-page'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('about/', views.about, name='about-page'),
    path('contact/', views.contactUsers, name='contact-page'),
    path('news/', views.news, name='news-page'),

]
