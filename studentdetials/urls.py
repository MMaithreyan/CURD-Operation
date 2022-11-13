from django.urls import path, include
from .import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.studentform, name='studentform'),
    path('list/', views.studentlist, name='studentlist'),
    path('list/delete/<int:id>', views.studentdelete, name='studentdelete'),
    path('list/edit/<int:id>', views.studentupdate, name='studentupdate'),
    path('list/edit/updaterecord/<int:id>',views.updaterecord, name='updaterecord'),
]
