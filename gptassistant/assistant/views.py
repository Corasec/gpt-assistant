from django.shortcuts import render
from django.http import HttpResponse
from assistant.models import Chat
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
from django.conf import settings

def home(request):
    return HttpResponse("The Home Page")


def error_handler(request):
    return HttpResponse("404 Page")


def GptChat(request):
    chats = Chat.objects.all()
    return render(
        request,
        "assistant/assistant.html",
        {
            "chats": chats,
        },
    )


@csrf_exempt
def AjaxView(request):
    if (
        request.headers.get("X-Requested-With") == "XMLHttpRequest"
    ):  # Check if request is Ajax
        text = request.POST.get("text")
        print("text: ", text)

        openai.api_key = settings.OPENIA_API_KEY
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{text}"}], max_tokens=1000,
        )

        response = res.choices[0].message["content"]
        print("txt_response: ", response)

        chat = Chat.objects.create(text=text, gpt=response)

        return JsonResponse(
            {
                "data": response,
            }
        )
    return JsonResponse({})
