import datetime

import rest_framework.status as status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotAcceptable
from django.contrib.auth.models import User
from ..auth import (IsCustomer, is_customer, is_delivery_crew,
                    is_manager)
from ..models import Cart, Order, OrderItem
from ..serializers import (OrderItemSerializer, OrderSerializer)

# Categories views


# Order management endpoints
# Order items
class OrdersView(generics.ListCreateAPIView):
    """
    Order management endpoints
    """
    queryset = Order.objects.prefetch_related(
        "orderitem_set").filter(user=4).all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["date", "total"]
    
    def get(self, request, *args, **kwargs):
        if is_manager(request):
            queryset = self.get_queryset
            serializer = OrderSerializer(queryset, many=True)
            return Response(serializer.data)

        elif is_delivery_crew(request):
            queryset = self.queryset.filter(delivery_crew=request.user.id)
            serializer = OrderSerializer(queryset, many=True)
            return Response(serializer.data)

        elif is_customer(request):
            queryset = self.queryset.filter(user=request.user.id)
            serializer = OrderSerializer(queryset, many=True)
            return Response(serializer.data)

        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        self.permission_classes = [IsCustomer]

        if is_customer(request):
            # Get the user's cart items
            cart_items = Cart.objects.filter(user=user)
            total_price = sum(item.price for item in cart_items)

            if len(cart_items) == 0:
                raise NotAcceptable("No cart items.")

            # Create a new order
            order = Order.objects.create(
                user=user,
                total=total_price,
                date=datetime.date.today()
            )

            # Create order items from the cart items
            order_items = []
            for cart_item in cart_items:
                order_item = OrderItem.objects.create(
                    order=order,
                    menuitem=cart_item.menuitem,
                    quantity=cart_item.quantity,
                    unit_price=cart_item.unit_price,
                    price=cart_item.price
                )
                order_items.append(order_item)

            # Delete the cart items for this user
            cart_items.delete()

            # Serialize the order and order items
            serializer = self.serializer_class(order)
            data = serializer.data
            data['order_items'] = OrderItemSerializer(
                order_items, many=True).data
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)


class SingleOrdersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def update_order(self, order, request, id):
        """Updates the order. A manager can use this endpoint to set a delivery crew to this order, and also update the order status to 0 or 1."""
        serializer = self.serializer_class(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def handle_put_patch(self, request, id):
        """
        Handles patching the single order item
        """
        if is_delivery_crew(request):
            order = get_object_or_404(
                Order, id=id, delivery_crew=request.user.id)
            if request.data.get("status"):
                order.status = request.data.get("status")
            return self.update_order(order, request, id=id)

        elif is_manager(request):
            order = get_object_or_404(Order, id=id)
            print(order)
            if request.data.get("status"):
                order.status = request.data.get("status")
            if request.data.get("delivery_crew"):
                user = get_object_or_404(
                    User, pk=request.data.get("delivery_crew"))
                order.delivery_crew = user
            return self.update_order(order, request, id=id)

        else:
            return Response({"message": "Unauthorized"}, status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk):
        return self.handle_put_patch(request=request, id=pk)

    def patch(self, request, pk):
        return self.handle_put_patch(request=request, id=pk)

    def get(self, request, *args, **kwargs):
        """
        For fetching the order item
        """
        if (is_customer(request)):
            order = get_object_or_404(
                Order, id=kwargs.get("pk"), user=request.user.id)
            serializer = self.serializer_class(order)
            return Response(serializer.data)
        elif is_delivery_crew(request):
            order = get_object_or_404(
                Order, id=kwargs.get("pk"), delivery_crew=request.user.id)
            serializer = self.serializer_class(order)
            return Response(serializer.data)
