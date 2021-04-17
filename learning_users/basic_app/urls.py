from django.urls import path,include
from basic_app import views

# as we are using template need to define the name which is simialr to basci_app
app_name='basic_app' 

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login')
    
]