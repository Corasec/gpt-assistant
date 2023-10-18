from django.urls import path
from assistant.views import AjaxView, error_handler, home, GptChat

# a list of all the urls
urlpatterns = [
    path("", home, name="home"),
    # path('new_chat/', views.new_chat, name='new_chat'),
    path("error-handler/", error_handler, name="error_handler"),
    path("ajax/", AjaxView, name="ajax"),
]
