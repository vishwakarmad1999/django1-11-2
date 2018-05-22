from django.conf.urls import url
from .views import (
        DishListView,
        DishDetailView,
        DishCreateView,
    )

urlpatterns = [
    url(r'^$', DishListView.as_view(), name = 'list'),
    url(r'^create/$', DishCreateView.as_view()),                    
    url(r'^(?P<slug>[-\w]+)/$', DishDetailView.as_view(), name = 'detail'),
]