from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.generic import RedirectView

from rest_framework import renderers

# card_list = CardViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# card_detail = CardViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# card_highlight = CardViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# collection_list = CollectionViewSet.as_view({
#     'get': 'list'
# })


urlpatterns = format_suffix_patterns([
    path('', RedirectView.as_view(url='/collections/')),
    path('cards/', views.CardList.as_view()),
    path('cards/<int:pk>/', views.CardDetail.as_view()),
    path('collections/<int:pk>/cards/', views.CollectionDetail.as_view()),
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:pk>/', views.CollectionList.as_view()),
])
