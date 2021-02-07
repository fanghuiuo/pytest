from django.db import models


# Create your models here.
class news(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    addtime = models.DateTimeField(auto_now_add=True)
    changetime = models.DateTimeField(auto_now=True)
    is_del = models.BooleanField(default=False)

    def __str__(self):
        return 'news:%s' % self.title
