from django.conf.urls import url

from .views import (
    BookList,
    BookDetail,
    BookCreation,
    BookUpdate,
    BookDelete
)

app_name = 'Book'

urlpatterns = [
    url(r'^$', BookList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', BookDetail.as_view(), name='detail'),
    url(r'^nuevo$', BookCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', BookUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', BookDelete.as_view(), name='delete'),
]