from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmPassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "name", "email", "password", "confirmPassword")

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data)
        user.set_password(
            validated_data[
                "password"])
        user.save()
        return user


class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email or password')
            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError('Both email and password are required')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', "email", 'name', 'job', 'location', 'about', 'phone', 'website', "is_superuser")


class UserListForAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')