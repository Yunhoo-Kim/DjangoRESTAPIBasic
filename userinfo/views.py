from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserSerializer, User
from helper.authentications import CustomJWTTokenAuthentication


class UserDetailView(APIView):
    authentication_classes = (CustomJWTTokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class UserCreateReadView(ListCreateAPIView):
    """
    get:
    # Return list of Users

    post:
    # make user instance
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


