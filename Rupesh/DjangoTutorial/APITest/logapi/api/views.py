from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response



class LoginApi(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        response_data = {}

        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            response_data["message"] = "Success"
            response_data["status"] = True
            response_data["data"] = {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        else:
            refresh = RefreshToken.for_user(user)
            response_data["message"] = " not provided."
            response_data["status"] = False
            response_data["data"] = {
                'access': str(refresh.access_token),
                'refresh': str(refresh),

            }
        return Response(response_data)