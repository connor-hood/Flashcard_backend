from rest_framework import viewsets, permissions, renderers, generics
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import CardSerializer, CollectionSerializer
from .models import Card, Collection


# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'collections': reverse('collection-list', request=request, format=format),
        'cards': reverse('card-list', request=request, format=format)
    })


class CardHighlight(generics.GenericAPIView):
    queryset = Card.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        card = self.get_object()
        return Response(card.highlighted)


class CollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        card = self.get_object()
        return Response(card.question)

    def perform_create(self, serializer):
        serializer.save()
# class CardList(generics.ListCreateAPIView):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#
#
# class CardDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#
#
# class CollectionList(generics.ListCreateAPIView):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer
#
#
# class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer
#

