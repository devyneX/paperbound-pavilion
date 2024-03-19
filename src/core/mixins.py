from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.cache import cache
from django.http import HttpRequest, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# Custom mixin to check if the user is a superuser
class SuperuserRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser


class CachedViewMixin:

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().get(request, *args, **kwargs)  # type: ignore

    @method_decorator(cache_page(60 * 60 * 2))
    def post(self, request, *args, **kwargs):
        cache.clear()
        return super().post(request, *args, **kwargs)
