from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.studentform, name='studentform'),
    path('list/', views.studentlist, name='studentlist'),
    path('delete/<int:id>', views.studentdelete, name='studentdelete'),
    path('edit/<int:id>', views.studentupdate, name='studentupdate'),
    path('edit/updaterecord/<int:id>',views.updaterecord, name='updaterecord'),
]
