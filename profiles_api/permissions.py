from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """permite al usuario editar su propio perfil"""
    def has_object_permission(self, request, view, obj):
        """chequea si el usuario esta intentando modificar su perfil"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """permite actualizar su propio perfil"""
    def has_object_permission(self, request, view, obj):
        """chequea si el usuario esta intentando modificar su perfil"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile_id == request.user.id

        