
from csv import field_size_limit
from dataclasses import fields
from pyexpat import model

from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import Department, Students


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','dept_id','dept_name','dept_head']

        def get_dept_name(self, obj):
            return '{} {}'.format(obj.dept_name, "Department")


class StudentAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ['id','first_name','last_name','department']


class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    department = DepartmentSerializer(many=True)

    class Meta:
        model = Students
        fields = ['id','std_id','first_name','last_name','full_name','department']

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)


class DepartmentSummarySerializer(serializers.Serializer):
    dept_name = serializers.CharField(max_length=100)
    student_count = serializers.IntegerField()


class NestedDepartmentSerializer(serializers.Serializer):
    dept_name = serializers.CharField(max_length=100)
    dept_id = serializers.IntegerField()
    dept_head = serializers.CharField()


class AddNestedStudentSerializer(serializers.ModelSerializer):
    department = NestedDepartmentSerializer(many=True)

    class Meta:
        model = Students
        fields = ['id','std_id','first_name','last_name','department']

    def create(self, validated_data):
        departments_data = validated_data.pop('department')
        student = Students.objects.create(**validated_data)
        for obj in departments_data:
            try:
                instance = Department.objects.create(**obj)
                student.department.add(instance)
                student.save()
            except IntegrityError:
                student.delete()
                raise ValidationError('Department Id already exist.')
        return student

    def update(self,instance, validated_data):

        departments_data = validated_data.pop('department')
        student = Students.objects.filter(id=instance.id).update(**validated_data)

        for obj in departments_data:

            if instance.department.filter(dept_id=obj['dept_id']):
                Department.objects.filter(dept_id=obj['dept_id']).update(**obj)
            else:
                dept_instance = Department.objects.create(**obj)
                instance.department.add(dept_instance)
                instance.save()
        return instance
