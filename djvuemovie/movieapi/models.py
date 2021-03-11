from django.db import models


# top250电影表
class Dbmovie(models.Model):
    dym = models.CharField(max_length=250, blank=True, null=True, verbose_name='电影名')
    dy = models.CharField(max_length=250, blank=True, null=True, verbose_name='导演')
    bj = models.CharField(max_length=250, blank=True, null=True, verbose_name='编剧')
    zy = models.TextField(blank=True, null=True, verbose_name='主演')
    lx = models.CharField(max_length=200, blank=True, null=True, verbose_name='类型')
    zpgj = models.CharField(max_length=200, blank=True, null=True, verbose_name='制片国家')
    yy = models.TextField(blank=True, null=True, verbose_name='语言')
    syrq = models.CharField(max_length=200, blank=True, null=True, verbose_name='上映日期')
    pc = models.CharField(max_length=200, blank=True, null=True, verbose_name='片长')
    ym = models.CharField(max_length=250, blank=True, null=True, verbose_name='原名')
    jqjj = models.TextField(blank=True, null=True, verbose_name='剧情简介')
    dbpf = models.CharField(max_length=45, blank=True, null=True, verbose_name='豆瓣评分')
    pjrs = models.CharField(max_length=200, blank=True, null=True, verbose_name='豆瓣评价人数')
    gfwz = models.CharField(max_length=250, blank=True, null=True, verbose_name='官方网站')
    pfzb = models.CharField(max_length=250, blank=True, null=True, verbose_name='评分占比')
    imdbpf = models.CharField(max_length=250, blank=True, null=True, verbose_name='imdb评分')
    imdbpjrs = models.CharField(max_length=45, blank=True, null=True, verbose_name='imdb评价人数')
    hjqk = models.TextField(blank=True, null=True, verbose_name='获奖情况')
    cybq = models.CharField(max_length=250, blank=True, null=True, verbose_name='常用标签')
    yjhpj = models.CharField(max_length=250, blank=True, null=True, verbose_name='一句话评价')

    class Meta:
        managed = True
        db_table = 'dbmovie'

    def __str__(self):
        return self.dym


# 用户表
class User(models.Model):

    user_type_choices = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP'),
    )
    user_sex_choices = ((1, '男'), (2, '女'))
    user_education_choices = (
        (1, '高中'),
        (2, '本科'),
        (3, '硕士'),
        (4, '博士'),
    )
    username = models.CharField(max_length=32, verbose_name='用户名', blank=True, null=True)
    userpassword = models.CharField(max_length=32, verbose_name='用户密码', blank=True, null=True)
    usersex = models.IntegerField(choices=user_sex_choices, verbose_name='性别', blank=True, null=True)
    usereducation = models.IntegerField(choices=user_education_choices, blank=True, null=True)
    userbirthday = models.DateField(verbose_name='用户密码', blank=True, null=True)
    roleid = models.IntegerField(blank=True, null=True, verbose_name='角色id')
    usertype = models.IntegerField(choices=user_type_choices, blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='状态', blank=True)
    createtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', blank=True, null=True)
    updatetime = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'User'

    def __str__(self):
        return self.username


# token表
class UserToken(models.Model):
    token = models.CharField(max_length=64)
    username = models.OneToOneField(to='User', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'UserToken'

    def __str__(self):
        return self.token


# 角色表
class Role(models.Model):
    # roleid = models.AutoField(primary_key=True)
    roleid = models.IntegerField(primary_key=True)
    rolename = models.CharField(max_length=50, blank=True, null=True, verbose_name='角色名称')
    roledec = models.CharField(max_length=50, blank=True, null=True, verbose_name='角色说明')
    pmids = models.IntegerField(blank=True, null=True, verbose_name='权限id集合')

    class Meta:
        managed = True
        db_table = 'Role'

    def __str__(self):
        return self.rolename


# 权限表
class Permission(models.Model):
    # pmid = models.AutoField(primary_key=True)
    pmid = models.IntegerField(primary_key=True)
    pm_pid = models.IntegerField(blank=True, null=True, verbose_name='父id')
    pmname = models.CharField(max_length=50, blank=True, null=True, verbose_name='权限名称')
    pmurl = models.CharField(max_length=100, blank=True, null=True, verbose_name='权限路径')
    pmlevel = models.IntegerField(blank=True, null=True, verbose_name='权限等级')  # 0是一级菜单，1是二级菜单，3是页面按钮级别
    pmaction = models.CharField(max_length=100, blank=True, null=True, verbose_name='操作动作')  # add,del,modify,search

    class Meta:
        managed = True
        db_table = 'Permission'

    def __str__(self):
        return self.pmname
