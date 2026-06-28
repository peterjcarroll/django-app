from django.contrib.sitemaps import Sitemap
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse


def is_htmx(request: HttpRequest) -> bool:
    return bool(request.headers.get("Hx-Request"))


def index(request: HttpRequest):
    if is_htmx(request):
        return render(request, "core/index.html#main-content")
    return render(request, "core/index.html")


class StaticViewSitemap(Sitemap):
    def items(self):
        return ["core:index"]

    def location(self, item):
        return reverse(item)


def robots_txt(request: HttpRequest) -> HttpResponse:
    protocol = "https" if request.is_secure() else "http"
    sitemap_url = f"{protocol}://{request.get_host()}/sitemap.xml"
    content = f"User-agent: *\nDisallow: /manage/\nSitemap: {sitemap_url}\n"
    return HttpResponse(content, content_type="text/plain")
