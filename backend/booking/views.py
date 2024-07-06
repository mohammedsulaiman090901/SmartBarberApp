from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, ServiceSerializer, BookingSerializer
from .models import CustomUser, Service, Booking
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
        if request.user.user_type != 3:
            return Response({"detail": "Unauthorized access."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"message": "Welcome to the Customer Dashboard!"})

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ShowSecretKey(APIView):
    def get(self, request):
        return Response({"secret_key": settings.SECRET_KEY})

class BarberListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(user_type=2)
    serializer_class = UserSerializer
