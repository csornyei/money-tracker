from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from tracker import views

urlpatterns = [
    path('spendings/', views.SpendingList.as_view(), name='get-post-spending'),
    path('spendings/<int:id>', views.SpendingDetail.as_view(), name='get-put-delete-spending')
]

urlpatterns = format_suffix_patterns(urlpatterns)
