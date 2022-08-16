from django.urls import path,include
from my_app import views

app_name = 'my_app'

urlpatterns = [
    path('registration/',views.registration,name='registration'),
    path('login/',views.user_login_view,name='login'),
    
]