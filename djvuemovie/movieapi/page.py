from rest_framework import pagination


class fenye(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
