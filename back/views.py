from back.serializers import CandidateSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from django.core.files.storage import default_storage
from back.api import candidates

# Create your views here.
#@csrf_exempt
#def departmentApi(request,id=0):
#    if request.method=='GET':
#        departments = Departments.objects.all()
#        departments_serializer = DepartmentSerializer(departments, many=True)
#        return JsonResponse(departments_serializer.data, safe=False)

#    elif request.method=='POST':
#        department_data=JSONParser().parse(request)
#        department_serializer = DepartmentSerializer(data=department_data)
#        if department_serializer.is_valid():
#            department_serializer.save()
#            return JsonResponse("Added Successfully!!" , safe=False)
#        return JsonResponse("Failed to Add.",safe=False)
@csrf_exempt
def addCandidate(request, id=0):
    pass

@csrf_exempt
def listCandidates(request, id=0):
    objects = candidates.list_candidates()
    serializer = CandidateSerializer(objects, many=True)
    return JsonResponse(serializer.data, safe=False)