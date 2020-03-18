from django.contrib.auth.views import LoginView as GenericLoginView

from .forms import AuthenticationForm


class LoginView(GenericLoginView):
    redirect_authenticated_user = True
    form_class = AuthenticationForm
    template_name = 'authentication/login_page.html'
