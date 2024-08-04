from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Inventory, Sale
from .serializers import ProductSerializer, InventorySerializer, SaleSerializer
import logging
from rest_framework.permissions import AllowAny

logger = logging.getLogger(__name__)


class HomePageView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response(
            {"message": "Welcome to the API home page tecnical test "},
            status=status.HTTP_200_OK,
        )


class RegisterUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductAPIView(APIView):
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Product created: {serializer.data}")
            return Response(
                {"message": "Product registered", "product_id": serializer.data["id"]},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id, format=None):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Product updated: {serializer.data}")
            return Response({"message": "Product updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryAPIView(APIView):
    def post(self, request, format=None):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Inventory registered/updated: {serializer.data}")
            return Response(
                {"message": "Inventory registered/updated"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaleAPIView(APIView):
    def post(self, request, format=None):
        data = request.data
        product = get_object_or_404(Product, id=data["product_id"])
        inventory = get_object_or_404(
            Inventory, product=product, warehouse=data["warehouse"]
        )
        if inventory.quantity >= data["quantity"]:
            inventory.quantity -= data["quantity"]
            inventory.save()
            sale = Sale.objects.create(
                product=product, quantity=data["quantity"], warehouse=data["warehouse"]
            )
            logger.info(f"Sale registered: {sale.id}")
            return Response({"message": "Sale registered"})
        else:
            logger.warning(f"Insufficient inventory for sale: {data}")
            return Response(
                {"message": "Insufficient inventory"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class SalesReportAPIView(APIView):
    def get(self, request, format=None):
        sales = Sale.objects.all()
        report = {}
        for sale in sales:
            product = sale.product.name
            if product not in report:
                report[product] = 0
            report[product] += sale.quantity
        return Response(report)
