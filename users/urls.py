from django.urls import path
from .views import SignupView, LogoutAPIView, LoginAPIView

urlpatterns = [  
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]