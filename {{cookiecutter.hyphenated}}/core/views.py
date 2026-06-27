from django.http import HttpRequest
from django.shortcuts import render


def is_htmx(request: HttpRequest) -> bool:
    return bool(request.headers.get("Hx-Request"))


def index(request: HttpRequest):
    if is_htmx(request):
        return render(request, "core/index.html#main-content")
    return render(request, "core/index.html")
