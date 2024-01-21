from .models import User


def create_user(self, username, email, password):
    user = User.models.create(username=username, email=email, password=password)
    return user
