from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('cards/', views.CardList.as_view()),
    path('', RedirectView.as_view(url='cards/')),
    path('cards/<int:pk>/', views.CardDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
