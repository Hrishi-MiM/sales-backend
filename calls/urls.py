from django.urls import path
from .views import CallList, CallDetail, LogList

urlpatterns = [
    path('', CallList.as_view(), name='call-list'),
    path('<int:id>/', CallDetail.as_view(), name='call-detail'),
    path('<int:call_id>/logs/', LogList.as_view(), name='log-list'),
]
