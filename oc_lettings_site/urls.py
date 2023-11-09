from django.contrib import admin
from django.urls import path
import sentry_sdk
from django.views.generic import TemplateView
from profiles import views as pviews
from lettings import views as lviews
from .views import index, sentry_
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


def custom_404(request, exception):
    sentry_sdk.capture_exception(exception)
    return TemplateView.as_view(template_name="404.html")(request)


handler404 = custom_404
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
    # Sentry debug
    path("sentry-debug/", sentry_),
]
urlpatterns += staticfiles_urlpatterns()
