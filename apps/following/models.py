from django.db import models
from django.conf import settings


class Relationship(models.Model):
    RELATIONSHIP_FOLLOWING = 1
    RELATIONSHIP_BLOCKED = 2
    RELATIONSHIP_STATUSES = (
        (RELATIONSHIP_FOLLOWING, 'Following'),
        (RELATIONSHIP_BLOCKED, 'Blocked'),
    )

    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status_for_print = 'follows' if self.status == 1 else 'blocked'
        return f'{self.from_user} {status_for_print} {self.to_user}'

    def add_relationship(self, user, status):
        relationship, created = Relationship.objects.get_or_create(
            from_user=self,
            to_user=user,
            status=status)
        return relationship

    def remove_relationship(self, user, status):
        Relationship.objects.filter(
            from_user=self,
            to_user=user,
            status=status).delete()
        return

    def get_relationships(self, status):
        return self.relationships.filter(
            to_user__status=status,
            to_user__from_user=self)

    def get_related_to(self, status):
        return self.related_to.filter(
            from_user__status=status,
            from_user__to_user=self)

    def get_following(self):
        return self.get_relationships(RELATIONSHIP_FOLLOWING)

    def get_followers(self):
        return self.get_related_to(RELATIONSHIP_FOLLOWING)
