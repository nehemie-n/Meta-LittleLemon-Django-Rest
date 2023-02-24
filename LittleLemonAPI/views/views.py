from django.shortcuts import render
from rest_framework import generics
from ..serializers import CartSerializer, AddManagerDeliveryCrewSerializer, UserSerializer, CategorySerializer, MenuItemSerializer, OrderItemSerializer, OrderSerializer
from ..models import Cart, Order, OrderItem, Category, MenuItem
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
import rest_framework.status as status
from ..auth import IsManager, is_admin, is_manager, is_delivery_crew, is_customer
from django.shortcuts import get_object_or_404
# Categories views


class CategoriesView(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    permission_classes = [IsAdminUser]


# Managers and crew members
class ManagersDeliveryCrewView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        try:
            group = Group.objects.get(name=kwargs.get("group"))
        except:
            return Response({"message": "Group not found"}, status.HTTP_404_NOT_FOUND)
        users = group.user_set.all()
        users = self.serializer_class(users, many=True).data
        return Response({"users": users})

    def post(self, request, *args, **kwargs):
        self.serializer_class = AddManagerDeliveryCrewSerializer

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(pk=request.data['id'])
        managers = Group.objects.get(name=kwargs.get("group"))
        managers.user_set.add(user)
        user.groups.add(managers)
        return Response({'success': True}, status.HTTP_201_CREATED)


class DeleteSingleManagersDeliveryCrew(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get('pk'))
        group = Group.objects.get(name=kwargs.get("group"))
        group.user_set.remove(user)
        user.groups.remove(group)
        return Response({'success': True}, status.HTTP_200_OK)


# Menu items

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if (is_manager(request) or is_admin(request)):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response({"message": "Only managers can access this."}, status=status.HTTP_403_FORBIDDEN)


class ViewSingleMenuItemView(generics.RetrieveAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
