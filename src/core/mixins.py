from django.contrib.auth.mixins import (
    PermissionRequiredMixin, UserPassesTestMixin
)
from django.core.cache import cache
from django.http import HttpRequest, HttpResponse

# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page


class OwnerRequiredMixin(PermissionRequiredMixin):

    def is_owner(self, request):
        raise NotImplementedError(
            f'{self.__class__.__name__} must implement is_owner()'
        )

    def dispatch(self, request, *args, **kwargs):
        if not self.is_owner(request):
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


# Custom mixin to check if the user is a superuser
class SuperuserRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser


class CachedViewMixin:

    # @method_decorator(cache_page(60 * 60 * 2))
    def dispatch(self, request, *args, **kwargs):
        self.cache_key = self.request.path
        return super().dispatch(request, *args, **kwargs)

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().get(request, *args, **kwargs)  # type: ignore

    def post(self, request, *args, **kwargs):
        # Invalidate cache for this specific URL
        cache.delete(self.cache_key)
        return super().post(request, *args, **kwargs)
