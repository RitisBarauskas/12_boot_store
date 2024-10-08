from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from goods.models import Category, Good
from .serializers import CategorySerializer, GoodReadSerializer, GoodWriteSerializer, UserReadSerializer, UserWriteSerializer, ReviewSerializer
from .permissions import IsCreatorOrReadOnly
from reviews.models import Review

User = get_user_model()


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UserReadSerializer
        return UserWriteSerializer

    def perform_create(self, serializer):
        serializer.save()


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
