from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer
from rest_framework import generics
from .models import Service, Booking
from .serializers import ServiceSerializer, BookingSerializer
from django.conf import settings

class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BarberDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.user_type != 2: 
            return Response({"detail": "Unauthorized access."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"message": "Welcome to the Barber Dashboard!"})

class CustomerDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.user_type != 1:
            return Response({"detail": "Unauthorized access."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"message": "Welcome to the Customer Dashboard!"})

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ShowSecretKey(APIView):
    def get(self, request):
        return Response({"SECRET_KEY": settings.SECRET_KEY})
