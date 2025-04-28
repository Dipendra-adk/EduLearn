from django.db import models

class CourseCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    teacher = models.ForeignKey('users.Instructor', on_delete=models.CASCADE)