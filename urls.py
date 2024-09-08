from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    # path('student/', views.post_student),
    # path('update-student/<id>/', views.update_student),
    # path('delete-student/<id>/', views.delete_student),
    path('generic-student/', views.StudentGeneric.as_view()),
    path('generic-student/<id>/', views.StudentGeneric1.as_view()),
    path('get-book/', views.get_book),
    path('student/', views.StudentAPI.as_view()),

]


