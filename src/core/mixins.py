from django.contrib.auth.mixins import UserPassesTestMixin


# Custom mixin to check if the user is a superuser
class SuperuserRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser
