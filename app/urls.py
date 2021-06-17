from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('add-transaction', views.AddTransaction)
router.register('spend-points', views.SpednPoints)
router.register('point-final-balance', views.PointFinalBalance)
router.register('spend-final-balance', views.SpendFinalBalance)


urlpatterns = [
    path('', include(router.urls)),
]
