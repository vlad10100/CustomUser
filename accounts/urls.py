from django.urls import path 
from .views import UserSignUpView, UserLogInView, HomePage

app_name = 'accounts'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup_page'),
    path('login/', UserLogInView.as_view(), name='login_page'),
    path('home/', HomePage.as_view(), name='home_page'),
]