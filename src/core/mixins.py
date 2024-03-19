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
    def dispatch(self, request, *args, **kwargs):
        self.cache_key = self.request.path
        return super().dispatch(request, *args, **kwargs)

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().get(request, *args, **kwargs)  # type: ignore

    def post(self, request, *args, **kwargs):
        # Invalidate cache for this specific URL
        cache.delete(self.cache_key)
        return super().post(request, *args, **kwargs)
