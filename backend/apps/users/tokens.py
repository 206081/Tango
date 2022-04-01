from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.users.models import User


class ActivateUserTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return f"{user.pk}{timestamp}{user.is_active}"


def create_activation_token_per_user(user: User) -> str:
    """
    Function to generate one time used Token for activate user.

    """

    return ActivateUserTokenGenerator().make_token(user)


def check_activation_token(user_pk: int, token: str) -> bool:
    """
    Function to check token per user.

    """
    return ActivateUserTokenGenerator().check_token(User.objects.get(pk=user_pk), token)


def send_activation_email(user: User, token: str) -> None:
    """
    Function to send activation email to user.

    """
    activation_link = settings.FRONTEND_ACTIVATION_URL_TEMPLATE.format(
        token=token, uid=urlsafe_base64_encode(force_bytes(user.pk))
    )
    send_mail(
        subject="Crash Course - Please activate your account",
        message=f"Follow this link to activate your account {activation_link}",
        from_email=settings.EMAIL_FROM,
        recipient_list=[
            user.email,
        ],
        fail_silently=False,
    )
