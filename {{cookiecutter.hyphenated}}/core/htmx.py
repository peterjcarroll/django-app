import functools

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def is_htmx(request: HttpRequest) -> bool:
    return bool(request.headers.get("Hx-Request"))


def is_htmx_fragment(request: HttpRequest) -> bool:
    """True for htmx partial-swap requests; False for hx-boost page navigations."""
    return is_htmx(request) and not request.headers.get("Hx-Boosted")


def htmx_form_view(full_template: str, fragments: dict):
    def decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(request: HttpRequest, *args, **kwargs):
            request.htmx = is_htmx(request)
            result = view_func(request, *args, **kwargs)
            if isinstance(result, HttpResponse):
                return result
            if isinstance(result, tuple):
                fragment_key, context = result
                if request.htmx:
                    return render(request, fragments[fragment_key], context)
                return render(request, full_template, context)
            return render(request, full_template, result)

        return wrapper

    return decorator
