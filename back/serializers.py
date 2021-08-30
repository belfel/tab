from rest_framework import serializers
from back.models import Candidates

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