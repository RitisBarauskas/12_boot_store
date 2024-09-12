from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from goods.models import Category, Good


User = get_user_model()


class UserReadSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GoodReadSerializer(ModelSerializer):
    category = CategorySerializer()
    creator = UserReadSerializer()

    class Meta:
        model = Good
        exclude = ('is_open_for_all',)


class GoodWriteSerializer(ModelSerializer):
    class Meta:
        model = Good
        exclude = ('is_open_for_all',)
        read_only_fields = ('creator',)

    def validate_description(self, value):
        if len(value) < 10:
            raise ValidationError('Минимальная длина описания - 10 символов.')
        return value

    def create(self, validated_data):
        validated_data['is_open_for_all'] = True
        return Good.objects.create(**validated_data)

    def to_representation(self, instance):
        return GoodReadSerializer(instance).data
