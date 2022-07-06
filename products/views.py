from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Product
from .serializers import GetProductsSerialier, PostProductSerializer
from .utils import GetPostCustomMixin
from .permissions import FreeGetPermission, IsSellerOwner

class ListCreateProductView(GetPostCustomMixin, ListCreateAPIView):

    permission_classes=[FreeGetPermission]

    queryset = Product.objects.all()
    serializer_map = {
        "GET": GetProductsSerialier,
        "POST": PostProductSerializer,
    }
    

class RetrieveUpdateProductView(GetPostCustomMixin, RetrieveUpdateAPIView):

    permission_classes=[IsSellerOwner]
    queryset = Product
    serializer_map = {
        "GET": GetProductsSerialier,
        "PATCH": PostProductSerializer,
    }