from rest_framework import permissions, viewsets

from .models import Account
from .serializers import AccountSerializer
from .permissions import IsAccountOwner


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permission(self):
        method = self.request.method
        if (method in permissions.SAFE_METHODS or method == 'POST'):
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)
