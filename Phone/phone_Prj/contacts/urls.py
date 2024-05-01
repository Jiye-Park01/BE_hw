from django.urls import path
from .views import ListView
from .views import *
from .views import create, detail, update, delete
# from .views import ResultView

urlpatterns = [
    # path('result/', ListView.as_view(), name="result"), 
    path('', ListView.as_view(), name="list"), 
    path('result/', result, name = 'result'),
    path('create/', create, name="create"), 
    path('detail/<int:id>/', detail, name = "detail"),
    path('update/<int:id>/', update, name = "update"),
    path('delete/<int:id>/', delete, name = "delete"),  
]
