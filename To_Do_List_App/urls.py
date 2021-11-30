from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('update/<int:update_pk>', views.update, name='update'),
    path('delete/<int:delete_pk>', views.delete, name='delete'),
    path('deleted_data/<int:deleted_data_pk>', views.deleted_data, name='deleted_data'),
    path('add/', views.add, name='add'),
    path('completed/<int:pk>', views.completed, name='completed'),
    path('updated_data/', views.updated_data, name='updated_data'),
]
