from django.contrib.auth.views import LoginView

from django.conf.urls import url, include
from django.contrib import admin
from restaurant.views import (
        HomeView,
        AboutView,
        RestaurantLocationCreateView,
        ContactView,
        CreatorView,
        Creator_2_View,
        )

from profiles.views import ProfileFollowToggle

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', LoginView.as_view(), name = 'login'),
    url(r'^$', HomeView.as_view(), name = 'home'),
    url(r'^about/$', AboutView.as_view(), name = 'about'),
    url(r'^contact/$', ContactView.as_view(), name = 'contact'),
    url(r'^creator/$', CreatorView.as_view(), name = 'divya'),    
    url(r'^creator2/$', Creator_2_View.as_view(), name = 'harsha'),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name = 'follow'),


    url(r'^restaurant/', include('restaurant.urls', namespace = 'restaurant')),
    url(r'^item/', include('menu.urls', namespace = 'item')),
    url(r'^u/', include('profiles.urls', namespace = 'profile')),
    ]