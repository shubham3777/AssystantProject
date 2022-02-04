from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('department/',views.DepartmentAdd.as_view()),
    path('department/<int:pk>/',views.DepartmentAdd.as_view()),
    path('student/',views.StudentInfo.as_view()),
    path('student/<int:pk>/',views.StudentInfo.as_view()),
    path('department-summary/',views.DepartmentSummary.as_view())
]