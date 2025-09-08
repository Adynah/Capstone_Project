from django.urls import path
from .views import RegisterView, UserView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('profile/', UserView.as_view(), name="user"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
