from rest_framework import pagination


class fenye(pagination.PageNumberPagination): #自定义分页
    page_size = 5
    page_query_param = 'page'
