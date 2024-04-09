from django.urls import path
from .views import ListView
from .views import *
# from .views import ResultView

urlpatterns = [
    # path('result/', ListView.as_view(), name="result"), 
    path('', ListView.as_view(), name="list"), 
    path('result/', result, name = 'result')
]
