from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from ..auth import (IsCustomer)
from ..models import Cart, MenuItem
from ..serializers import (CartSerializer)


# Cart management endpoints
# Cart
class CartItemsView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsCustomer]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get(self, request, *args, **kwargs):
        carts = self.queryset.filter(user=request.user)
        serializer = self.serializer_class(carts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        item = get_object_or_404(MenuItem, id=request.data["menuitem"])
        cart = request.data
        cart["user"] = request.user.id
        cart["unit_price"] = item.price
        cart["price"] = (cart.get("quantity") or 0) * item.price

        serializer = self.serializer_class(data=cart)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        user = request.user.id
        self.queryset.filter(user=user).delete()
        return Response({"message": "Deleted"})
