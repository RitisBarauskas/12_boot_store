from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from goods.models import Category, Good
from .serializers import CategorySerializer, GoodReadSerializer, GoodWriteSerializer
from .permissions import IsCreatorOrReadOnly


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GoodViewSet(ModelViewSet):
    queryset = Good.objects.all()
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GoodReadSerializer
        return GoodWriteSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user, is_open_for_all=True)
