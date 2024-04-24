from api_v1.serializers.users import UserCreateSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import User


class UsersViewSet(ModelViewSet):
    """
    Viewset модели пользователя.
    """

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer
        return UserCreateSerializer
