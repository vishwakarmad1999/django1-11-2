"""MuyPicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from restaurant.views import (
        HomeView,
        AboutView,
        RestaurantLocationCreateView,
        ContactView,
        CreatorView,
        Creator_2_View,
        SearchRestaurantListView,
        SearchRestaurantDetailView,
        DishListView,
        DishDetailView,
        DishCreateView,
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^about/$', AboutView.as_view()),
    url(r'^restaurant/create/$', RestaurantLocationCreateView.as_view()),
    url(r'^contact/$', ContactView.as_view()),
    url(r'^creator/$', CreatorView.as_view()),    
    url(r'^creator2/$', Creator_2_View.as_view()),
    #url(r'^restaurant/(?P<slug>[-\w]+)/$', SearchRestaurantListView.as_view()),
    url(r'^restaurant/(?P<slug>[-\w]+)/$', SearchRestaurantDetailView.as_view()),
    url(r'^restaurant/$', SearchRestaurantListView.as_view()),
    url(r'^dish/$', DishListView.as_view()),
    url(r'^dish/create/$', DishCreateView.as_view()),                    
    url(r'^dish/(?P<slug>[-\w]+)/$', DishDetailView.as_view()),
]