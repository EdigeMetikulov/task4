from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CourseListView, CourseView
app_name = "courses312"

router = DefaultRouter()


urlpatterns = [
    path('', CourseListView.as_view(), name='courses_list'),
    path('<int:pk>', CourseView.as_view(), name='course_view')
]
