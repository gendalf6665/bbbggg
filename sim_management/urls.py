from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'sim_management'  # Добавляем пространство имен

router = DefaultRouter()
router.register(r'simcards', views.SimCardViewSet)
router.register(r'bots', views.ExternalBotViewSet)

urlpatterns = [
    path('', views.sim_card_list, name='sim_card_list'),
    path('simcard/<int:pk>/', views.sim_card_detail, name='simcard_detail'),
    path('api/', include(router.urls)),
]