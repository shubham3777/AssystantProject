
from django.http.response import Http404
from rest_framework.views import APIView

from Department.models import Students, Department
from .serializers import DepartmentSerializer, DepartmentSummarySerializer, StudentAddSerializer, StudentSerializer, \
    AddNestedStudentSerializer
from rest_framework.response import Response

from Department import serializers
from django.db.models import Count

# Create your views here.

class DepartmentAdd(APIView):

    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = DepartmentSerializer(data)

        else:
            data = Department.objects.all()
            serializer = DepartmentSerializer(data, many=True)

        return Response(serializer.data)

    def post(self,request,format=None):
        data = request.data
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200'})

    def put(self,request,pk,format=None):
        data = request.data
        dept = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(instance=dept,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'Department Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self,request,pk,format=None):
        data = request.data
        dept = Department.objects.get(pk=pk)
        dept.delete()
        res = {'msg' : 'Department deleted Successfully'}
        return Response(res)


class StudentInfo(APIView):
    serializer_class = AddNestedStudentSerializer

    def get_object(self, pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise Http404

    def post(self,request):
        data = request.data
        serializer = AddNestedStudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200'})
        else:
            return Response({'status': '400', 'errors': serializer.errors})

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = StudentSerializer(data)

        else:
            data = Students.objects.all()
            serializer = StudentSerializer(data, many=True)

        return Response(serializer.data)


    def put(self,request,pk,format=None):
        data = request.data
        student = Students.objects.get(pk=pk)
        serializer = AddNestedStudentSerializer(instance=student,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'Student Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self,request,pk,format=None):
        data = request.data
        student = Students.objects.get(pk=pk)
        student.delete()
        res = {'msg' : 'Department deleted Successfully'}
        return Response(res)



class DepartmentSummary(APIView):

    def get(self,request):
        departments = Department.objects.all().annotate(student_count=Count('students'))
        serializer = DepartmentSummarySerializer(departments,many=True)

        return Response({"status":"200","data":serializer.data})

