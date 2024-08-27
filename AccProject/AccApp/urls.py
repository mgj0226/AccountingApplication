from django.urls import path, include
from rest_framework import routers
from .views import AccountViewSet, CategoryViewSet, TransactionViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api', include(router.urls)),
]
