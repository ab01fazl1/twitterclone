from .models import Relationship


def get_follower(user_pk):
    return Relationship.objects.filter(from_user=user_pk)


def get_follower_count(user):
    return Relationship.objects.filter(from_user=user).count()


def get_following(user):
    return Relationship.objects.filter(to_user=user)


def get_following_count(user):
    return Relationship.objects.filter(to_user=user).count()


def get_blocked(user):
    return Relationship.objects.filter(
        from_user=user, status=Relationship.RELATIONSHIP_STATUSES.BLOCKED
    )


# def create_realtionship(user, to_user, status):
# Relationship.objects
