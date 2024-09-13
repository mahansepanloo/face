from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

class Login(TokenObtainPairView):
    pass
class Refresh(TokenRefreshView):
    pass
