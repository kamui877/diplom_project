from django.urls import path, include
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from orders.views import RegisterAccount, ConfirmAccount, PartnerUpdate, PartnerState, PartnerOrders, CategoryView, \
    ShopView, ProductView, ProductInfoView, BasketView, ContactView, OrdersView, OrderView, OrderLastScreenView

app_name = 'orders'
urlpatterns = [
    path('', TemplateView.as_view(template_name='orders/home.html'), name='home'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='orders:schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='orders:schema'), name='redoc'),
    path('user/', include('django.contrib.auth.urls')),
    path('user/register/', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm/<uidb64>/<token>', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/contact', ContactView.as_view(), name='contacts'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
    path('product', ProductView.as_view(), name='products'),
    path('product/<id>', ProductInfoView.as_view(), name='product-info'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrdersView.as_view(), name='orders'),
    path('order/<id>', OrderView.as_view(), name='order'),
    path('confirmed', OrderLastScreenView.as_view(), name='order-confirmed'),

]