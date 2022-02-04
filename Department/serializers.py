
from csv import field_size_limit
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Department, Students


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','dept_name','dept_head']


class StudentAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ['id','first_name','last_name','department']


class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    department = DepartmentSerializer(many=True,read_only=True)

    class Meta:
        model = Students
        fields = ['id','first_name','full_name','department']
    

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)


class DepartmentSummarySerializer(serializers.Serializer):
    dept_name = serializers.CharField(max_length=100)
    student_count = serializers.IntegerField()