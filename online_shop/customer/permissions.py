from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from core.models import User


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method is SAFE_METHODS:
            return True
        else:
            return request.user.phone.endswith('76')