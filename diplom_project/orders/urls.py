from django.urls import path, include
from django.views.generic import TemplateView

from orders.views import RegisterAccount, PartnerUpdate, ConfirmAccount

app_name = 'orders'
urlpatterns = [
    path('', TemplateView.as_view(template_name='orders/home.html'), name='home'),
    path('user/', include('django.contrib.auth.urls')),
    path('user/register/', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),

]