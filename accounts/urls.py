from django.urls import path,include
from . import views
from rest_framework.authtoken import views as auth_token

app_name = 'accounts'

urlpatterns = [
    path('register/',views.UserRegister.as_view()),
    path('api-token-auth/', auth_token.obtain_auth_token )
]

