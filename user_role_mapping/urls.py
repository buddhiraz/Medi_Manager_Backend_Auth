from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserRoleMappingViewSet 


router = SimpleRouter()
router.register('', UserRoleMappingViewSet,)
urlpatterns = router.urls