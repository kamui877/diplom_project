from django.urls import path, include
from django.views.generic import TemplateView

from orders.views import RegisterAccount, PartnerUpdate, ConfirmAccount, PartnerOrders, CategoryView, \
    ShopView

app_name = 'orders'
urlpatterns = [
    path('', TemplateView.as_view(template_name='orders/home.html'), name='home'),
    path('user/', include('django.contrib.auth.urls')),
    path('user/register/', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm/<uidb64>/<token>', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),

]