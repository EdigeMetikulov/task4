from django.contrib import admin
from django import forms

from .models import Course, Contact, Category, Branch


class CourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.fields]
    search_fields = [field.name for field in Course._meta.fields]
    list_filter = [field.name for field in Course._meta.fields]


class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]
    search_fields = [field.name for field in Contact._meta.fields]
    list_filter = [field.name for field in Contact._meta.fields]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    search_fields = [field.name for field in Category._meta.fields]
    list_filter = [field.name for field in Category._meta.fields]


class BranchAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Branch._meta.fields]
    search_fields = [field.name for field in Branch._meta.fields]
    list_filter = [field.name for field in Branch._meta.fields]


admin.site.register(Course, CourseAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Branch, BranchAdmin)

admin.site.site_title = "Courses312 Admin panel"
admin.site.site_header = "Courses312 Admin panel"
