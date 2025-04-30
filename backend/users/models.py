from django.db import models

class Instructor(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)


class Learner(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    interested_categories = models.ManyToManyField('courses.CourseCategory')