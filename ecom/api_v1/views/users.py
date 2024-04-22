from api_v1.serializers.users import UserCreateSerializer, UserSerializer
from djoser.views import UserViewSet
from rest_framework.permissions import AllowAny
from users.models import User


class UsersViewSet(UserViewSet):
    """
    Viewset модели пользователя из Djoser.
    """

    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer
        return UserCreateSerializer
