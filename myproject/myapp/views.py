from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import YourModel
from .serializers import YourModelSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.
def home(request):
    return render(request,"home.html")



class Categories(APIView):
    @swagger_auto_schema(
        request_body=YourModelSerializer,
        responses={201: 'Data saved successfully', 400: 'Bad request'}
    )
    def post(self, request, *args, **kwargs):
        print("Request data:", request.data)
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            print("Valid data:", serializer.validated_data)
            serializer.save()
            print("Data saved successfully")
            return Response({'message': 'Data saved successfully'}, status=status.HTTP_201_CREATED)
        print("Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
        responses={200: YourModelSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        instances = YourModel.objects.all()
        serializer = YourModelSerializer(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
