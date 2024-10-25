from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated

from .models import Contestant
from .serializers import ContestantSerializer

from django.core.signing import Signer, BadSignature
from django.conf import settings

import random

class LastesContestantsList(APIView):
    def get(self, request, format=None):
        contestant = Contestant.objects.all()[0:3]
        serializer = ContestantSerializer(contestant, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def random_contestant_email(request):
    contestants = Contestant.objects.all()
    if not contestants:
        return Response({'error': 'No contestants found'}, status=404)

    random_contestant = random.choice(contestants)
    return Response({'email': random_contestant.email})

class ContestantRegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')

     
        if Contestant.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ContestantSerializer(data=request.data)
        if serializer.is_valid():
            contestant = serializer.save()

            signer = Signer()
            token = signer.sign(contestant.email)

            
            verification_link = f'http://localhost:8080/verify-email/{token}/'
            send_mail(
                'Verify your email',
                f'Please verify your email by clicking the following link: {verification_link}',
                settings.EMAIL_HOST_USER,  
                [contestant.email],
                fail_silently=False,
            )

            return Response({'message': 'User registered. Please verify your email.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyEmailView(APIView):
    def get(self, request, token):
        signer = Signer()

        try:
           
            email = signer.unsign(token)
            contestant = Contestant.objects.get(email=email)

            if not contestant.verified:
                contestant.verified = True
                contestant.save()
                return Response({'message': 'Email verified successfully. You may now set your password.', 'redirect_url': '/email-verification'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Email already verified'}, status=status.HTTP_400_BAD_REQUEST)

        except (BadSignature, Contestant.DoesNotExist):
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)
        


class SetPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        print("Email recibido en la solicitud:", email)

        try:
            contestant = Contestant.objects.get(email=email)

            if not contestant.verified:
                return Response({'error': 'Email not verified'}, status=status.HTTP_400_BAD_REQUEST)

            contestant.set_password(password)
            contestant.save()
            return Response({'message': 'Password set successfully'}, status=status.HTTP_200_OK)

        except Contestant.DoesNotExist:
            return Response({'error': 'Invalid email'}, status=status.HTTP_404_NOT_FOUND)



class ContestantLoginView(APIView):
  def post(self, request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
      contestant = Contestant.objects.get(email=email)
      if check_password(password, contestant.password):  
        return Response({
          'message': 'Login successful',
        }, status=status.HTTP_200_OK)
      else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except Contestant.DoesNotExist:
      return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)