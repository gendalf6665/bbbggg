from django.urls import path
from .views import SimCardListView, SimCardDetailView

app_name = 'sim_management'

urlpatterns = [
    path('', SimCardListView.as_view(), name='simcard_list'),
    path('simcard/<int:pk>/', SimCardDetailView.as_view(), name='simcard_detail'),
]