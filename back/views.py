from django.contrib import auth
from back import serializers
from back.serializers import CandidateSerializer, WorkerSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, HttpResponseBase, HttpResponseNotAllowed, HttpResponseServerError, JsonResponse
from django.contrib.auth import authenticate as auth_login
from django.core.files.storage import default_storage
from back.api import candidates, workers
from django.contrib.auth.models import User


@csrf_exempt
def addCandidate(request, id=0):
    data = JSONParser().parse(request)
    serializer = CandidateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("ok", safe=False)
    return JsonResponse("error", safe=False)

@csrf_exempt
def listCandidates(request, id=0):
    objects = candidates.list_candidates()
    serializer = CandidateSerializer(objects, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def register(request):
    login = request.GET.get('login', '')
    email = request.GET.get('email', '')
    password = request.GET.get('password', '')
    user = User.objects.create_user(login, email, password)
    user.save()
    worker = workers.add_worker("test", login, "test2", "2000-01-01", "")
    return JsonResponse("ok", safe=False)

@csrf_exempt
def authenticate(request):
    login = request.GET.get('login', '')
    password = request.GET.get('password', '')
    user = auth_login(username=login, password=password)
    if user is not None:
        worker = workers.get_worker_by_username(user.get_username())
        worker_serializer = WorkerSerializer(worker, many=False)
        return JsonResponse(worker_serializer.data, safe=False)
    else:
        return JsonResponse("login or password incorrect", safe=False)