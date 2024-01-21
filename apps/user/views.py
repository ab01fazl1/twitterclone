# from django.shortcuts import render
# from rest_framework.views import APIView
# from .serializers import UserSerializer
# from rest_framework.generics import CreateAPIView
# from .models import User
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import viewsets
#
# # class CreateUserView(CreateAPIView):
# #
# #     model = User.objects.all()
# #     # permission_classes = [
# #     #     permissions.AllowAny # Or anon users can't register
# #     # ]
# #     serializer_class = UserSerializer
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     # TODO define permission classes
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     # TODO define lookup_field
#
# # TODO partial update needs custom logic
#     # we can have PATCH on both user and profile with different logics
