from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from courses312 import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # path('api/courses312/', include('courses312.urls')),
                  path('api/courses', views.CoursesList.as_view()),
                  path('api/courses/<int:pk>', views.CoursesDetail.as_view()),



              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
