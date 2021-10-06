from rest_framework import serializers

from courses312.models import Category, Branch, Contact, Course


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [field.name for field in Category._meta.fields]


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = [field.name for field in Branch._meta.fields]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [field.name for field in Contact._meta.fields]


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    branches = BranchSerializer()
    contacts = ContactSerializer()

    class Meta:
        model = Course
        fields = [field.name for field in Course._meta.fields]
