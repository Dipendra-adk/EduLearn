from .import views
from django.urls import path


urlpatterns = [
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>', views.CourseDetail.as_view()),
    path('categories/', views.CourseCategoryList.as_view()),
    path('categories/<int:pk>', views.CourseCategoryDetail.as_view()),
]
