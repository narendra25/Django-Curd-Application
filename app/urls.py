from django.urls import path
from app import views
urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('insert/',views.insertedData),
    path('update/<id>',views.update),
    path('delete/<id>',views.delete),
]