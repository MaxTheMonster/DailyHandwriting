from django.conf.urls import url
from django.contrib import admin
from challenges import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^old/$', views.OldChallengesView.as_view(), name="old_challenges"),
    url(r'^admin/', admin.site.urls),
]
