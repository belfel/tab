from django.urls import path
from back import views


urlpatterns=[
    path('AddCandidate', views.addCandidate, name='addCandidate'),
    path('ListCandidates', views.listCandidates, name='listCandidates'),
]