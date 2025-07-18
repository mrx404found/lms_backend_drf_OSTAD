from django.urls import path
from .views import (
    category_list_create,
    course_list_create,
    course_detail,
    lesson_list_create,
    material_list_create,
    enrollment_list_create,
    question_list_create,
    mark_lesson_completed,
    enroll_course,
)

urlpatterns = [
    path("categories/", category_list_create, name="category-list-create"),
    path("courses/", course_list_create, name="course-list-create"),
    path("courses/<int:pk>/", course_detail, name="course-detail"),
    path("lessons/", lesson_list_create, name="lesson-list-create"),
    path("materials/", material_list_create, name="material-list-create"),
    path("enrollments/", enrollment_list_create, name="enrollment-list-create"),
    path("questions/", question_list_create, name="question-list-create"),
    path(
        "lessons/<int:lesson_id>/complete/",
        mark_lesson_completed,
        name="mark-lesson-completed",
    ),
    path('courses/<int:course_id>/enroll/', enroll_course, name='enroll-course'),
]
