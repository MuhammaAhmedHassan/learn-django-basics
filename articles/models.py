from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    # pic = models.ImageField(upload_to='blah', default='path/to/my/default/image.jpg')
    # add in author
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        isGreaterThan50 = self.body.__len__() >= 50
        return self.body[:50] + "..."  if isGreaterThan50 else self.body
        # return self.body[:50] # from start to 50th characters


# commands after make or changing the model
# python3 manage.py makemigrations
# python3 manage.py migrate

# To interact with the database using ORM
# python3 manage.py shell

# 1. We need to create a super user to login to the admin panel
# python3 manage.py createsuperuser
