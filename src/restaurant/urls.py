from django.conf.urls import url

from .views import (
        RestaurantLocationCreateView,
        SearchRestaurantListView,
        SearchRestaurantDetailView,
        RestaurantUpdateView
    )

urlpatterns = [
    url(r'^create/$', RestaurantLocationCreateView.as_view()),
    #url(r'^(?P<slug>[-\w]+)/update/$', RestaurantUpdateView.as_view(), name = 'update'),
    url(r'^(?P<slug>[-\w]+)/$', RestaurantUpdateView.as_view(), name = 'detail'),
    url(r'^$', SearchRestaurantListView.as_view(), name='list'),
]