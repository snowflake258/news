from django.urls import path
from management import views


app_name = 'management'
urlpatterns = [
    path('category/list/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('article/list/', views.ArticleListView.as_view(), name='article_list'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/update/<int:pk>/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>/', views.ArticleDeleteView.as_view(), name='article_delete'),

    path('article-image/list/<int:article_pk>/', views.ArticleImageListView.as_view(), name='article_image_list'),
    path('article-image/create/', views.ArticleImageCreateView.as_view(), name='article_image_create'),
    path('article-image/delete/<int:pk>/', views.ArticleImageDeleteView.as_view(), name='article_image_delete')
]
