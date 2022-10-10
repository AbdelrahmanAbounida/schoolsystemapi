from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .classView import (
                StudentDetail,
                StudentList,
                TeacherList,
                SubjectList,
                StudentListGeneric,
                StudntListMixin,
                TeacherUpdateGeneric,
                TeacherCreateGeneric,
                SubjectListMixin
            )

urlpatterns = [
    path('students/',StudentList.as_view(),name='students list'),
    path('students_mixins/',StudntListMixin.as_view(),name='StudntListMixin'),
    path('teachers/',TeacherList.as_view(),name='teachers list'),
    path('subjects/',SubjectList.as_view(),name='subjects list'),
    path('student/<int:pk>',StudentDetail.as_view(),name='student detail'),
    path('student_generic_list/',StudentListGeneric.as_view(),name="student_generic_list"),
    path('teacher-generic/<int:pk>',TeacherUpdateGeneric.as_view(),name="teacher generic"),
    path('teacher-create',TeacherCreateGeneric.as_view(),name="TeacherCreateGeneric"),
    path('subject-mixin/<int:pk>',SubjectListMixin.as_view(),name="SubjectListMixin"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
