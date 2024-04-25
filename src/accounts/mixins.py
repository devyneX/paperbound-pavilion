from django.contrib.auth.mixins import UserPassesTestMixin


class UnauthenticatedRequiredMixin(UserPassesTestMixin):
    raise_exception = True
    permission_denied_message = 'You are already authenticated.'

    def test_func(self):
        return not self.request.user.is_authenticated
