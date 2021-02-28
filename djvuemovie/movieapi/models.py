from django.db import models


class Dbmovie(models.Model):
    dym = models.CharField(max_length=250, blank=True, null=True)
    dy = models.CharField(max_length=250, blank=True, null=True)
    bj = models.CharField(max_length=250, blank=True, null=True)
    zy = models.TextField(blank=True, null=True)
    lx = models.CharField(max_length=200, blank=True, null=True)
    zpgj = models.CharField(max_length=200, blank=True, null=True)
    yy = models.TextField(blank=True, null=True)
    syrq = models.CharField(max_length=200, blank=True, null=True)
    pc = models.CharField(max_length=200, blank=True, null=True)
    ym = models.CharField(max_length=250, blank=True, null=True)
    jqjj = models.TextField(blank=True, null=True)
    dbpf = models.CharField(max_length=45, blank=True, null=True)
    pjrs = models.CharField(max_length=200, blank=True, null=True)
    gfwz = models.CharField(max_length=250, blank=True, null=True)
    pfzb = models.CharField(max_length=250, blank=True, null=True)
    imdbpf = models.CharField(max_length=250, blank=True, null=True)
    imdbpjrs = models.CharField(max_length=45, blank=True, null=True)
    hjqk = models.TextField(blank=True, null=True)
    cybq = models.CharField(max_length=250, blank=True, null=True)
    yjhpj = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dbmovie'

    def __str__(self):
        return self.dym


class User(models.Model):
    user_type_choices = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP'),
    )
    usertype = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=32)
    userpassword = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'User'

    def __str__(self):
        return self.username


class UserToken(models.Model):
    token = models.CharField(max_length=64)
    username = models.OneToOneField(to='User', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'UserToken'

    def __str__(self):
        return self.token
