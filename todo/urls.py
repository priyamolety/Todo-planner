from django .urls import path
from todo.views import home, updatetask, deletetask

urlpatterns = [
    path('',home, name="list"),
    path('update/<str:pk>/', updatetask, name = "updatetask"),
    path('delete/<str:pk>/', deletetask, name="delete"),
]