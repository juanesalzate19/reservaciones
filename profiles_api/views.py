from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from profiles_api import serializers, models, permissions


class HelloApiview(APIView):
    """api view de prueba"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """retornar vistas de caracteristicas del apiview"""
        an_apiview = [
            'usamos metodos http como funciones(get,post,delete,put,patch)',
            'es similar a una vista tradicional de django',
            'nos da el mayor control sobre la logica de nuestra aplicacion',
            'esta el mapeo manualmente de los urls',
        ]
        """ASI SE DEFINE UN APIVIEW EN UNA FUNCION GET"""
        return Response({'message': 'hello',  'an_apiview': an_apiview})

    def post(self, request):
        """crea un mensaje con nuestro nombre"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola  {name}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """maneja actualizar un objeto"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """maneja actualizacion parcial de un objeto"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """borar un objeto"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """retornar mensaje de hola mundo"""
        a_viewset = [
            'usa acciones(list, create,retrive, update, partial_update)',
            'automaticamente mapea a los urls usando routers',
            'provee mas funcionalidad con menos codigo',
        ]
        return Response({'message': 'hola!', 'a_viewset': a_viewset})

    def create(self, request):
        """vamos a crear nuevo mensaje de hola mundo"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hola {name}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """OBTIENE UN OBJETO Y SU ID """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ACTUALIZA UN OBJETO"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ACTUALIZA PRINCIPALMENTE UN OBJETO"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """DESTRUYE UN OBJETO"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """crear y actualizar perfiles"""

    def delete(self, request, pk=None):
        """borar un objeto"""
        return Response({'method': 'DELETE'})
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    def create(self, request):
        body = request.data
        user = serializers.UserProfileSerializer(data=body)
        if user.is_valid():
            user_created = user.save()
            return Response(status=201, data={f'user created {user_created.name}'})
        else:
            return Response(status=400, data={"the user could not be created"})


class UserLoginApiView(ObtainAuthToken):
    """crea tokens de autenticacion del usuario"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """maneja el crear leer y actualizar el profile feed"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """se encarga de setear el perfil de usuario para el usuario que esta logeado"""
        serializer.save(user_profile=self.request.user)


class SillasProfileViewSet(viewsets.ModelViewSet):
    """crear y actualizar perfiles"""

    def destroy(self, request, id):
        """borar un objeto"""
        print(id)
        queryset = models.SillasProfile.delete(id)
        return Response({'method': 'DELETE'})

    def put(self, request):
        """maneja actualizar un objeto"""
        return Response({'method': 'PUT'})

    serializer_class = serializers.SillasProfieSerializer
    queryset = models.SillasProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('silla',)
