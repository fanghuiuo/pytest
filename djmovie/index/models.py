from django.db import models


class Dbmovie(models.Model):
    dym = models.CharField(max_length=45, blank=True, null=True)
    dy = models.CharField(max_length=100, blank=True, null=True)
    bj = models.CharField(max_length=100, blank=True, null=True)
    zy = models.CharField(max_length=200, blank=True, null=True)
    lx = models.CharField(max_length=100, blank=True, null=True)
    zpgj = models.CharField(max_length=100, blank=True, null=True)
    yy = models.CharField(max_length=100, blank=True, null=True)
    syrq = models.CharField(max_length=100, blank=True, null=True)
    pc = models.CharField(max_length=100, blank=True, null=True)
    ym = models.CharField(max_length=100, blank=True, null=True)
    jj = models.TextField(blank=True, null=True)
    dbpf = models.CharField(max_length=100, blank=True, null=True)
    pjrs = models.CharField(max_length=100, blank=True, null=True)
    yjhpj = models.CharField(max_length=250, blank=True, null=True)
    gfwz = models.CharField(max_length=250, blank=True, null=True)
    imdbpf = models.CharField(max_length=250, blank=True, null=True)
    imdbpjrs = models.CharField(max_length=250, blank=True, null=True)
    pfzb = models.CharField(max_length=250, blank=True, null=True)
    cybq = models.CharField(max_length=250, blank=True, null=True)