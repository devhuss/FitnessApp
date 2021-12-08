from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.create_workout, name="create_workout"),
    path('delete/<int:id>', views.delete_workout, name='delete_workout'),
    path('update/<int:id>', views.update_workout, name='update_workout'),
    path('contact', views.contact, name='contact'),
    path('log', views.log, name='log')
    ]
