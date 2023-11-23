from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .tasks import send_email

@api_view(['POST'])
def register(request):
    user = User.objects.create(
        name=request.data['name'],
        email=request.data['email']
    )
    send_email.delay(user.id)
    return Response(status=201)


@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)