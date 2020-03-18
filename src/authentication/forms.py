from django.contrib.auth.forms import AuthenticationForm
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        # Неактивные пользователи не смогут войти
        if not user.is_active:
            raise ValidationError(
                _('Account is inactive.'),
                code='inactive'
            )
