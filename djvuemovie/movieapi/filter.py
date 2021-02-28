import django_filters
from .models import Dbmovie, User


class moviefilter(django_filters.FilterSet):
    # 大于这个值 name指定字段 lookup_expr过滤条件
    # NumberFilter 数字类型 豆瓣评分大于小于
    # api url 就是/movie/?dbpf_min=8&dbpf_max=9
    # dbpf_min = django_filters.NumberFilter(field_name="dbpf", lookup_expr="gte")
    # 小于这个值    gt 大于 gte 大于等于  lt小于 lte 小于等于
    # dbpf_max = django_filters.NumberFilter(field_name="dbpf", lookup_expr="lte")

    # name模糊查询, 不指定过滤条件, 必须全部匹配
    # CharFilter字符串类型 如下指定过滤条件 模糊匹配
    # dym = django_filters.CharFilter(field_name="dym", lookup_expr="icontains")

    # 使用 API 查询是原来的 url 是/movie/, 模糊查询的 url 就变成/movie/?dym__icontains=xxx

    class Meta:
        # 指定模型类
        model = Dbmovie
        # 显示这两个字段
        # fields = ['dbpf_min', 'dbpf_max', 'dym']

        fields = {
            'dym': ['icontains'],
            'dy': ['icontains'],
            'bj': ['icontains'],
            'lx': ['icontains'],
            'zpgj': ['icontains'],
            'yy': ['icontains'],
            'gfwz': ['icontains'],
            'cybq': ['icontains'],
            # 或者这么表达imdbpf大于小于 gt 大于 gte 大于等于  lt小于 lte 小于等于
            # 可以这样来进行大小范围搜索/movie/?imdbpf__gte=8.4&imdbpf__lte=9
            'pjrs': ['gte', 'lte'],
            'imdbpjrs': ['gte', 'lte'],
            'dbpf': ['gt', 'lt'],
            'imdbpf': ['gt', 'lt'],
        }


class userfilter(django_filters.FilterSet):

    class Meta:
        model = User
        fields = ['username', 'userpassword']
