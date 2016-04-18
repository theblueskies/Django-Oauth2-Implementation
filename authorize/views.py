from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from app_permissions import IsAuthenticatedOrCreate
from serializers import SignUpSerializer
from rest_framework import permissions
from django.http import Http404 

# Create your views here.

# This endpoint is protected. You can access it by passing in the token with the GET request.
class RestrictedListUserEndpoint(APIView):
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request, *args, **kwargs):
    usernames = [user.username for user in User.objects.all()]
    return Response(usernames)

# This endpoint will allow all access for signing-up.
class SignUp(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = SignUpSerializer
  permission_classes = (IsAuthenticatedOrCreate,)

