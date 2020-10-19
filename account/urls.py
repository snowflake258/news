from django.urls import path
from account import views


app_name = 'account'
urlpatterns = [
    path('sign-in/', views.SignInView.as_view(), name='sign_in'),
    path('sign-out/', views.SignOutView.as_view(), name='sign_out'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up')
]
