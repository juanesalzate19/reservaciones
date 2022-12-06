from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """serializa un campo para probar nuestra api"""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """serializa objeto de perfil de usuario"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style': {'input_type':'password'}

            }
        }

    def create(self, validate_data):
        """crear y retornar nuevo usuario"""
        user = models.UserProfile.objects.create_user(
            email = validate_data['email'],
            name = validate_data['name'],
            password = validate_data['password']
        )

        return user



    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """serializador de profile feed item"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only':True}}

class SillasProfieSerializer(serializers.ModelSerializer):
    """serializa objeto de perfil de usuario"""
    class Meta:
        model = models.SillasProfile
        fields = ('id', 'fecha', 'silla')
        

    def create(self, validate_data):
        """crear y retornar nuevo usuario"""
        user = models.SillasProfile.object.create_silla(
            fecha = validate_data['fecha'],
            silla = validate_data['silla'],
        )

        return user