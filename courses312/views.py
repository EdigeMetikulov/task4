from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import Http404

from courses312.models import Category, Course, Contact, Branch
from courses312.serializers import CategorySerializer, CourseSerializer, ContactSerializer, BranchSerializer

from rest_framework.views import APIView


class CoursesList(APIView):

    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class CoursesDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

































# class CategoryViewSet(ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CourseViewSet(ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# class ContactViewSet(ModelViewSet):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
#
# class BranchViewSet(ModelViewSet):
#     queryset = Branch.objects.all()
#     serializer_class = BranchSerializer
