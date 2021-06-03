from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('cards/', views.CardList.as_view()),
    path('', RedirectView.as_view(url='cards/')),
]
