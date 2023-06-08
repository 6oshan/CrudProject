from crudapp import views
from django.urls import path

urlpatterns = [
    path('', views.demo,name='demo'),
    path('delete/<int:crudid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    # path('mylist/',views.MyModelList.as_view(),name='mylist'),
    ]
 


