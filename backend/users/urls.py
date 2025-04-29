from django.urls import path
from . import views

urlpatterns = [
    path('instructors/', views.InstructorView.as_view()),
    # path('instructors/<int:pk>', views.InstructorDetail.as_view()),
    path('learners/', views.LearnerView.as_view()),
    # path('learners/<int:pk>', views.LearnerDetail.as_view()),
]