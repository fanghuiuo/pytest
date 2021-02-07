from django.db import models


class Dbbook(models.Model):
    bookname = models.CharField(max_length=200, blank=True, null=True)
    yjhpj = models.CharField(max_length=200, blank=True, null=True)
    dbpf = models.CharField(max_length=200, blank=True, null=True)
    pjrs = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    cbs = models.CharField(max_length=200, blank=True, null=True)
    cbn = models.CharField(max_length=200, blank=True, null=True)
    ys = models.CharField(max_length=200, blank=True, null=True)
    dj = models.CharField(max_length=200, blank=True, null=True)
    zz = models.CharField(max_length=200, blank=True, null=True)
    cs = models.CharField(max_length=200, blank=True, null=True)
    isbn = models.CharField(max_length=200, blank=True, null=True)
    nrjj = models.TextField(blank=True, null=True)
    zzjj = models.TextField(blank=True, null=True)
    cpf = models.CharField(max_length=200, blank=True, null=True)
    fbt = models.CharField(max_length=200, blank=True, null=True)
    yzm = models.CharField(max_length=200, blank=True, null=True)
    yz = models.CharField(max_length=200, blank=True, null=True)
    addtime = models.DateTimeField(auto_now_add=True)
    changetime = models.DateTimeField(auto_now=True)
