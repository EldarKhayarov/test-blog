from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin


class IsOwnerMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.username == kwargs['slug']:
            return super().dispatch(request, args, kwargs)
        return self.handle_no_permission()


class IsNotOwnerMixin(LoginRequiredMixin):
    pass
