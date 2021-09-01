from rest_framework import serializers
from back.models import Candidates, Workers
from django.contrib.auth.models import User

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidates
        fields = ('ID',
                  'Name',
                  'Surname',
                  'Birthdate',
                  'Application_date',
                  'Phone_number',
                  'Sex',
                  'Email_address',
                  'CV',
                  'Motivation_letter',
                  'Hired',
                  )

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ('ID',
                 'Name',
                 'Surname',
                 'Birthdate',
                 'Login',
                 #'Password',
                 'Email_address',
                 'ID_Workers_Role',
                 )