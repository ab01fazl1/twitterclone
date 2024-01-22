from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status

from apps.user.models import User, Profile
from apps.user.services import create_user
from api.serializers.users import GetUserSerializer, UserSerializer, ProfileSerializer


class CreateUserView(GenericAPIView, CreateModelMixin):

    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        confirm_password = serializer.validated_data["confirm_password"]

        if password == confirm_password:
            create_user(username, email, password)
        else:
            return Response("wrong password", status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetUserView(GenericAPIView, RetrieveModelMixin):

    queryset = User.objects.all()
    serializer_class = GetUserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UpdateUserView:
    def partial_update(self, request, *args, **kwargs):
        pass


class UpdateProfileView:
    def partial_update(self, request, *args, **kwargs):
        pass


# write a function based view for reset password
class ResetPasswordView:
    pass
