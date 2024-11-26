from django.utils.translation import gettext_lazy
from rest_framework.pagination import PageNumberPagination

from config import settings


class HabitPaginator(PageNumberPagination):
    page_size = settings.PAGE_SIZE
    page_size_query_param = "page_size"
    max_page_size = settings.MAX_PAGE_SIZE
    page_size_query_description = gettext_lazy('Количество результатов, возвращаемых на страницу')
