from learning.views import *
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("student/", StudentAPI.as_view(), name="student"),
    path("teacher", TeacherView.as_view(), name="teacher"),
    path("university", UniversityView.as_view(), name="university"),
    path("drinks/", drink_list),
    path("drinks/<int:id>", drink_details),
    path("register/", RegisterUser.as_view()),

    path("generic-student/", StudentGeneric.as_view()),
    path("generic-student/<id>/", StudentGenericNew.as_view()),
    path("pdf/", GeneratePdf.as_view()),

    path("", homePage),
]

urlpatterns = format_suffix_patterns(urlpatterns)