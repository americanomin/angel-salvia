from django.conf.urls import url
from chatbots.views import home_keyboard, message

urlpatterns = [
    url(r'^keyboard', home_keyboard),
    url(r'^message', message),
]