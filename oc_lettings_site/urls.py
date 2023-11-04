from django.contrib import admin
from django.urls import path

from profiles import views as pviews
from lettings import views as lviews
from .views import index

urlpatterns = [
    # Index url is the welcome page at 127.0.0.1/
    path("", index, name="index"),
    # Display all the lettings at 127.0.0.1/lettings/
    path("lettings/", lviews.index, name="lettings_index"),
    # Display a letting page with its information.
    path("lettings/<int:letting_id>/", lviews.letting, name="letting"),
    # Display all the profiles at 127.0.0.1/profiles/
    path("profiles/", pviews.index, name="profiles_index"),
    # Display a profile page with its information.
    path("profiles/<str:username>/", pviews.profile, name="profile"),
    # Admin URL.
    path("admin/", admin.site.urls),
]
