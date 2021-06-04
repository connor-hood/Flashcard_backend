from .models import Card
from .serializers import CardSerializer
from rest_framework import generics, renderers
from rest_framework.response import Response


# Create your views here.
class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardHighlight(generics.GenericAPIView):
    queryset = Card.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        card = self.get_object()
        return Response(card.highlighted)