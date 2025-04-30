from django.urls import path
from . import views

urlpatterns = [
    path('instructors/', views.InstructorList.as_view()),
    path('instructors/<int:pk>', views.InstructorDetail.as_view()),
    path('learners/', views.LearnerList.as_view()),
    path('learners/<int:pk>', views.LearnerDetail.as_view()),
    
]