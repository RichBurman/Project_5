from django.db import models
from django.contrib.auth import get_user_model
from packages.models import Package


class Review(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    star_rating = models.PositiveIntegerField(choices=[(
        1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} for {self.package.title}"
