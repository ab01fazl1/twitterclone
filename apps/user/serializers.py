# from rest_framework import serializers
# from .models import User, Profile
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth import get_user_model
#
# class UserCreateSerializer(serializers.ModelSerializer):
#
#     password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
#     confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True,
#                                              label='Confirm password')
#
#     email = serializers.EmailField(validators=[
#         UniqueValidator(
#             queryset=get_user_model().objects.all(),
#             message="This email is already in use.",
#         )]
#     )
#
#     class Meta:
#             model = User
#             fields = ['username', 'email', 'password', 'confirm_password']
#
#     def validate(self, attrs):
#         password = attrs['password']
#         confirm_password = attrs['confirm_password']
#         if password != confirm_password:
#             raise serializers.ValidationError(
#                 {
#                     'password': "Error: The passwords didn't match"
#                 }
#             )
#
#         return attrs
#
#     def create(self, validated_data):
#         username = validated_data['username']
#         email = validated_data['email']
#         password = validated_data['password']
#
#         user = self.Meta.model(username=username, email=email)
#         user.set_password(password)
#         user.save()
#         return user
#
# class ProfileViewSerializer(serializers.ModelSerializer):
#     follower_count = serializers.SerializerMethodField()
#     following_count = serializers.SerializerMethodField()
#
#     # we have a TweetsOfUserSerializer in tweet.serializers
#     # tweets = serializers
#
#     class Meta:
#         model = Profile
#         fields = ['user', 'description', 'birthday', 'following_count', 'follower_count']
#
#     def get_follower_count(self):
#         pass
#
#     def get_following_count(self):
#         pass
#
#
# class UserUpdateSerializer(serializers.ModelSerializer):
#     # TODO we can update username, email and password
#         # but password reset and email change calls a service to send SMS (with celery)
#         # username can be changed noramlly
#     pass
#
# class ProfileUpdateSerializer(serializers.ModelSerializer):
#     # TODO we can change desc, birthday
#     pass
#
# class UserDeleteSerializer(serializers.ModelSerializer):
#     # also deletes profile class
#     pass
#
# class UserListSerializer(serializers.ModelSerializer):
#     # TODO retreive a list of users. the queryset could be anything
#     pass
