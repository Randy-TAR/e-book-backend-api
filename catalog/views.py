from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from django.http import JsonResponse
from asgiref.sync import sync_to_async
from services.ai_services import summarize_book, generate_tags

# Create your views here.

class AdminLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user and user.is_staff:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })

        return Response({"error": "Invalid credentials"}, status=401)



async def summarize_view(request):
    text = request.GET.get("text", "")
    result = await summarize_book(text)
    return JsonResponse(result)

def summarize_book_view(request):
    text = request.GET.get("text", "")
    if not text:
        return JsonResponse({"error": "No text provided"}, status=400)

    result = summarize_book(text)
    return JsonResponse(result)

def generate_tags_view(request):
    text = request.GET.get("text", "")
    if not text:
        return JsonResponse({"error": "No text provided"}, status=400)

    result = generate_tags(text)
    return JsonResponse(result)