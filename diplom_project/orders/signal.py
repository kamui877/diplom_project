from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver, Signal

from orders.models import ConfirmEmailToken, CustomUser


new_user_registered = Signal()


@receiver(new_user_registered)
def new_user_registered_signal(user_id, **kwargs):

    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        f"Password Reset Token for {token.user.email}",
        # message:
        token.key,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [token.user.email]
    )
    msg.send()


