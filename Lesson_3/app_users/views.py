from rest_framework.viewsets import ModelViewSet
from .models import UserModel
from .serialiazers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
