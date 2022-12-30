import jwt
import requests
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import User


class JWTLogIn(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:
            token = jwt.encode(
                {"pk": user.pk},
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            return Response({"token": token})
        else:
            return Response({"error": "wrong password"})


class LogOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "다음에 또 만나요"})


class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"ok": "Welcome"})
        else:
            return Response({"error": "잘못된 패스워드 입니다. "})


class PublicUser(APIView):
    def get(self, request, username):
        user = User.objects.get(username=username)
        serializer = serializers.PublicUserSerializer(
            user,
        )
        return Response(serializer.data)


class Users(APIView):
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError("비밀번호를 작성해야 합니다.")

        serializer = serializers.PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Me(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            raise ParseError

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GithubLogIn(APIView): 

  def post(self, request): 
    try: 
      code = request.data.get("code")
      access_token = requests.post(f"https://github.com/login/oauth/access_token?code={code}&client_id=d3d9977c152c50bddaa4&client_secret={settings.GH_SECRET}", 
      headers={"Accept": "application/json"},
      )

      access_token = access_token.json().get("access_token")
      user_data = requests.get(
        "https://api.github.com/user", 
        headers={
            "Authorization": f"Bearer {access_token}", 
            "Accept": "application/json"
        },
      )
      user_data = user_data.json()

      try: 
        user = User.objects.get(email=user_data.get("email"))
        login(request, user)
        return Response(status=status.HTTP_200_OK)
      except User.DoesNotExist: 
        user = User.objects.create(
          username=user_data.get("login"), 
          email=user_data.get("email"), 
          name=user_data.get("name"), 
          avatar=user_data.get("avatar_url")
        )
        user.set_unusable_password()
        user.save()
        login(request, user)
        return Response(status=status.HTTP_200_OK)
    except Exception: 
      return Response(status=status.HTTP_400_BAD_REQUEST)



class KakaoLogIn(APIView): 
  def post(self, request): 
    try: 
      code = request.data.get("code")
      access_token = requests.post("https://kauth.kakao.com/oauth/token", 
        headers={
          "Content-Type": "application/x-www-form-urlencoded"
        }, 
        data={
          "grant_type": "authorization_code", 
          "client_id": "c00c9350689f948254a3cc6207a83134", 
          "redirect_uri": "http://127.0.0.1:3000/social/kakao", 
          "code": code,
        }
      )
      access_token = access_token.json().get("access_token")

      user_data = requests.get("https://kapi.kakao.com/v2/user/me", 
        headers={
          "Authorization": f"Bearer ${access_token}", 
          "Content-type": "application/x-www-form-urlencoded",
        }
      )
      user_data = user_data.json()
      kakao_account = user_data.get("kakao_account")
      profile = kakao_account.get("profile")

      try: 
        user = User.objects.get(email=kakao_account.get("email"))
        login(request, user)
        return Response(status=status.HTTP_200_OK)
      except User.DoesNotExist: 
        user = User.objects.create(
          email=kakao_account.get("email"),
          username=profile.get("nickname"),
          name=profile.get("nickname"),
          avatar=profile.get("profile_image_url"),
        )
        user.set_unusable_password()
        user.save()
        login(request, user)
        return Response(status=status.HTTP_200_OK)
    except Exception:
      return Response(status=status.HTTP_400_BAD_REQUEST)

