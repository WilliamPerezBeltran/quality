
from django.contrib import admin
from django.urls import path
from inventory.views import (
    ProductAPIView,
    InventoryAPIView,
    SaleAPIView,
    SalesReportAPIView,
    HomePageView,
    RegisterUserAPIView,
)
from inventory.auth_views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    custom_obtain_auth_token,
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('product/', ProductAPIView.as_view(), name='product'),
    path('product/<int:product_id>/', ProductAPIView.as_view(), name='update_product'),
    path('inventory/', InventoryAPIView.as_view(), name='inventory'),
    path('sale/', SaleAPIView.as_view(), name='sale'),
    path('sales-report/', SalesReportAPIView.as_view(), name='sales_report'),
    # Token authentication endpoints
    path('api-token-auth/', custom_obtain_auth_token, name='api_token_auth'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
