from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def credits(request):
    content = "Nicky\nMarc"

    return HttpResponse(content, content_type="text/plain")


def about(request):
    content = "<html><body><p>hello</p></body></html>"

    return HttpResponse(content)


def version(request):
    content = {
        'version': '1.0.0',
    }

    return JsonResponse(content, json_dumps_params={'indent': 4})


def news(request):
    data = {
        'news': [
            "RiffMates now has a news page!",
            "RiffMates has its first web page",
        ],
    }

    return render(request, "news2.html", data)


def news_advanced(request):
    data = {
        'news': [
            (date(2017, 3, 12), "RiffMates now has a news page!"),
            (date(2024, 6, 1), "RiffMates has its first web page"),
        ],
    }

    return render(request, "news_advanced.html", data)
