from django.urls import path
from news_site import views


app_name = 'news_site'
urlpatterns = [
    path('', views.StartPage.as_view(), name='start_page'),
    path('start-page/', views.StartPage.as_view(), name='start_page'),
    path('start-page/<int:category>/', views.StartPage.as_view(), name='start_page'),
    path('article/detail/<int:pk>/', views.ArticleDetail.as_view(), name='article_detail')
]
