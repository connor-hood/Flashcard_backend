from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.generic import RedirectView
from .views import CardViewSet, CollectionViewSet, api_root
from rest_framework import renderers

card_list = CardViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
card_detail = CardViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
card_highlight = CardViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
collection_list = CollectionViewSet.as_view({
    'get': 'list'
})
collection_detail = CollectionViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('cards/', card_list, name='card-list'),
    path('cards/<int:pk>/', card_detail, name='card-detail'),
    path('collections/<int:pk>/cards/', card_highlight, name='card-highlight'),
    path('collections/', collection_list, name='collection-list'),
    path('collections/<int:pk>/', collection_detail, name='collection-detail')
])
