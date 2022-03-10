from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from dj_auth.api.serializers import NoteSerializer
from dj_auth.models import Note

from dj_auth.api.permissions import IsOwnerOrReadOnly




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer













class Routes(APIView):
    def get(self, request):
        routes = [
            'api/token',
            'api/token/refresh'
        ]

        return Response(data=routes)


class NoteView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get(self, request):
        user = request.user
        data = user.note_set.all()
        serializer = self.serializer_class(instance=data, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)