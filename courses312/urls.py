from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CategoryViewSet, BranchViewSet, ContactViewSet, CourseListView, CourseView
app_name = "courses312"
from . import views

router = DefaultRouter()
router.register("Category", views.CategoryViewSet)
router.register("Branch", views.BranchViewSet)
router.register("Contact", views.ContactViewSet)

urlpatterns = [
    path('', CourseListView.as_view(), name='courses_list'),
    path('<int:pk>', CourseView.as_view(), name='course_view')
]
