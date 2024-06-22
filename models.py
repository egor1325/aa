from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class VideoPost(models.Model):
    status_choices = [
        (-1, 'decline'),
        (0, 'in process'),
        (1, 'published')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='videos/thumbnail/', default='none')
    category = models.CharField(max_length=50, default='none')
    pub_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)
    video_views = models.ManyToManyField(User, related_name='video_views', blank=True)
    status = models.IntegerField(max_length=2, choices=status_choices)

    def __str__(self):
        return self.title

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    profile_pic = models.ImageField(upload_to='pic/', default='pic/default.jpg')
    subscribers = models.ManyToManyField(User, related_name='subscribers')

class Comment(models.Model):
    post = models.ForeignKey(VideoPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username
