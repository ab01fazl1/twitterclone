from django.db import models
from django.conf import settings


class Relationship(models.Model):
    FOLLOWING = 1
    BLOCKED = 2
    RELATIONSHIP_STATUSES = (
        (FOLLOWING, "Following"),
        (BLOCKED, "Blocked"),
    )

    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="following", on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="follower", on_delete=models.CASCADE
    )
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status_for_print = "follows" if self.status == 1 else "blocked"
        return f"{self.from_user} {status_for_print} {self.to_user}"
