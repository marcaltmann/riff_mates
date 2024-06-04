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
