from django.http import HttpResponse
from django.test import RequestFactory, TestCase

from core.htmx import htmx_form_view, is_htmx, is_htmx_fragment


class IsHtmxTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_returns_true_when_hx_request_header_present(self):
        request = self.factory.get("/", HTTP_HX_REQUEST="true")
        self.assertTrue(is_htmx(request))

    def test_returns_false_without_hx_request_header(self):
        request = self.factory.get("/")
        self.assertFalse(is_htmx(request))


class IsHtmxFragmentTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_returns_true_for_htmx_request_without_boost(self):
        request = self.factory.get("/", HTTP_HX_REQUEST="true")
        self.assertTrue(is_htmx_fragment(request))

    def test_returns_false_for_hx_boosted_navigation(self):
        request = self.factory.get("/", HTTP_HX_REQUEST="true", HTTP_HX_BOOSTED="true")
        self.assertFalse(is_htmx_fragment(request))


class HtmxFormViewDecoratorTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_attaches_htmx_true_for_htmx_request(self):
        captured = {}

        @htmx_form_view(full_template="core/index.html", fragments={})
        def view(request):
            captured["htmx"] = request.htmx
            return HttpResponse()

        request = self.factory.get("/", HTTP_HX_REQUEST="true")
        view(request)
        self.assertTrue(captured["htmx"])

    def test_attaches_htmx_false_for_plain_request(self):
        captured = {}

        @htmx_form_view(full_template="core/index.html", fragments={})
        def view(request):
            captured["htmx"] = request.htmx
            return HttpResponse()

        request = self.factory.get("/")
        view(request)
        self.assertFalse(captured["htmx"])

    def test_passes_through_httpresponse_unchanged(self):
        sentinel = HttpResponse("sentinel", status=302)

        @htmx_form_view(full_template="core/index.html", fragments={})
        def view(request):
            return sentinel

        request = self.factory.get("/")
        response = view(request)
        self.assertIs(response, sentinel)

    def test_renders_fragment_for_htmx_tuple_result(self):
        @htmx_form_view(
            full_template="core/index.html",
            fragments={"main": "core/index.html#main-content"},
        )
        def view(request):
            return "main", {}

        request = self.factory.get("/", HTTP_HX_REQUEST="true")
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"<html", response.content)

    def test_renders_full_template_for_non_htmx_tuple_result(self):
        @htmx_form_view(
            full_template="core/index.html",
            fragments={"main": "core/index.html#main-content"},
        )
        def view(request):
            return "main", {}

        request = self.factory.get("/")
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<html", response.content)
