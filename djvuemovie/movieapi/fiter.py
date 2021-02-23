from django_filters import rest_framework as filtrs
from .models import Dbmovie


class moviefiter(filtrs.filterset):

    """
    过滤类
    """

    # 大于这个值 name指定字段 lookup_expr过滤条件
    # NumberFilter 数字类型 豆瓣评分大于小于
    # api url 就是/movie/?dbpf_min=8&dbpf_max=9
    dbpf_min = filtrs.NumberFilter(name="dbpf", lookup_expr="gte")
    # 小于这个值
    dbpf_max = filtrs.NumberFilter(name="dbpf", lookup_expr="lte")

    # name模糊查询, 不指定过滤条件, 必须全部匹配
    # CharFilter字符串类型 如下指定过滤条件 模糊匹配
    dym = filtrs.CharFilter(name="dym", lookup_expr="icontains")
    # 使用 API 查询是原来的 url 是/movie/, 模糊查询的 url 就变成/movie/?dym__icontains=xxx

    class Meta:
        # 指定模型类
        model = Dbmovie
        # 显示这两个字段
        # fields = ["price_min", "price_max", "dym"]
        fields = {
            'gfwz': ['icontains'],
            # 或者这么表达imdbpf大于小于
            #  可以这样来进行大小范围搜索/movie/?imdbpf__gte=8.4&imdbpf__lte=9
            'imdbpf': ['gte', 'lte'],

        }

