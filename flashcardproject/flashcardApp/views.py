from django.shortcuts import render
from .models import Card
from .serializers import CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CardList(APIView):

    def get(self, request):
        card = Card.objects.all()
        serializer = CardSerializer(card, many=True)
        return Response(serializer.data)