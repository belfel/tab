from rest_framework import serializers
from back.models import Candidates
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('ID',
                'Login'
                 )