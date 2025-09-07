from rest_framework import generics, permissions
from .models import User
from .serializers import RegisterSerializer, UserSerializer

# Registration endpoint
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Endpoint to retrieve logged-in user info
class UserView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
