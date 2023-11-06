from django.shortcuts import render
from profiles.models import Profile
import logging


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def index(request):
    """
    Display index page with all profiles information.
    :param request:
    :return: request template profiles with context.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)
    except:
        logging.error("No profiles list")
        logging.info("No profiles list found at profiles.views.index")
        context = {"profile": "profiles list"}
        return render(request, "500.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis,
# pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis
# fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue. Pellentesque habitant
# morbi tristique senectus et netus et males
def profile(request, username):
    """
    Display a profile page.
    :param request:
    :param username:
    :return: request template profile with context.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except:
        logging.error(f"No profile {username}")
        logging.info(f"No profile {username} found in profiles.views.profile")
        context = {"profile": username}
        return render(request, "500.html", context)
