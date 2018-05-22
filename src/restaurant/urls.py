from django.conf.urls import url

from .views import (
        RestaurantLocationCreateView,
        SearchRestaurantListView,
        SearchRestaurantDetailView,
    )

urlpatterns = [
    url(r'^create/$', RestaurantLocationCreateView.as_view()),
    url(r'^(?P<slug>[-\w]+)/$', SearchRestaurantDetailView.as_view(), name = 'detail'),
    url(r'^$', SearchRestaurantListView.as_view(), name='list'),
]