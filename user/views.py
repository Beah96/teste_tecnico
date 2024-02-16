from .models import User
from rest_framework.generics import CreateAPIView
from .serializer import UserSerializer

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
