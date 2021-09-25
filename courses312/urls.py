from rest_framework.routers import DefaultRouter
# from courses.courses312.views import CategoryViewSet, CourseViewSet, ContactViewSet, BranchViewSet
from .import views

app_name = "courses312"

router = DefaultRouter()
# router.register("Category", views.CategoryViewSet)
# router.register("Course", views.CourseViewSet)
# router.register("Contact", views.ContactViewSet)
# router.register("Branch", views.BranchViewSet)

urlpatterns = router.urls

# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from courses312 import views
#
# urlpatterns = [
#     path('', views.CoursesList.as_view()),
#     path('/<int:pk>/', views.CoursesDetail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)