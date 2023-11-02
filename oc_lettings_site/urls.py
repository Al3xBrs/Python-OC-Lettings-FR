from django.contrib import admin
from django.urls import path

from profiles import views as pviews
from lettings import views as lviews
from .views import index

urlpatterns = [
    path("", index, name="index"),
    path("lettings/", lviews.index, name="lettings_index"),
    path("lettings/<int:letting_id>/", lviews.letting, name="letting"),
    path("profiles/", pviews.index, name="profiles_index"),
    path("profiles/<str:username>/", pviews.profile, name="profile"),
    path("admin/", admin.site.urls),
]
