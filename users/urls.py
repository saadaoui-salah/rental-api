from django.urls import path
from .views import SignupView, LogoutAPIView, LoginAPIView, StatesView

urlpatterns = [  
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('states/', StatesView.as_view(), name='state'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]