'''inventory_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''

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
