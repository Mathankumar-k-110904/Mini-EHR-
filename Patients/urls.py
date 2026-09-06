from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("add/", views.add_patient, name="add_patient"),
    path("patients/", views.patient_list, name="patient_list"),
    path("patients/<int:id>/", views.patient_detail, name="patient_detail"),
    path("patients/<int:id>/edit/", views.edit_patient, name="edit_patient"),
    path("patients/<int:id>/delete/",views.delete_patient,name="delete_patient"),
]