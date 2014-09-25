__author__ = 'ahmetdal'


class AuthService():
    def __init__(self):
        pass


    @staticmethod
    def register_bulk_user_object_permissions(users, objects, permissions):

        count = 0
        for user in users:
            for object in objects:
                for permission in permissions:
                    AuthService.register_user_object_permissions(user,object,permission)
                    count += 1
        return count


    @staticmethod
    def register_user_object_permissions(user, object, permission):
        from guardian.models import UserObjectPermission

        UserObjectPermission.objects.assign_perm(permission.codename, user=user, obj=object)