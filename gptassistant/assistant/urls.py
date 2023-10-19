from django.urls import path
from assistant.views import AjaxView, error_handler, home, GptChat

app_name = "assistant"
urlpatterns = [
    # path("", home, name="home"),
    path("", GptChat, name='gpt_chat'),
    path("error-handler/", error_handler, name="error_handler"),
    path("ajax/", AjaxView, name="ajax"),
]
