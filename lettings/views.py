import logging

from django.shortcuts import render
from lettings.models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu. Vestibulum ante ipsum primis
# in faucibus orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Display lettings index page.
    :param request:
    :return: render request for the lettings_index page with all lettings list.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {"lettings_list": lettings_list}
        return render(request, "lettings/index.html", context)
    except Letting.DoesNotExist:
        context = {"profile": "No lettings list"}
        logging.error("No lettings list")
        return render(request, "500.html", context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas
# auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna.
# Suspendisse potenti. In tempus a nisi sed laoreet. Suspendisse porta dui eget sem accumsan
# interdum. Ut quis urna pellentesque justo mattis ullamcorper ac non tellus. In tristique
# mauris eu velit fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero,
# eget bibendum lorem. Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis nisi
# ligula. Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Display letting page.
    :param request:
    :param letting_id: letting id from the previous section.
    :return: render request for the letting page.
    """
    try:
        c_letting = Letting.objects.get(id=letting_id)
        context = {
            "title": c_letting.title,
            "address": c_letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Letting.DoesNotExist:
        logging.error(f"Can't find '{letting_id}' letting")
        context = {"profile": letting_id}
        return render(request, "500.html", context)
