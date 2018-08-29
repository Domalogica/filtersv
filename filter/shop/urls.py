from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^merchant/', include('django_tinkoff_merchant.urls')), # callback
    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    # url(r'^$', views.ProductList, name='ProductList'),
    url(r'^$', views.teles, name='main'),
    url(r'tele$', views.tele, name='tele'),
]