from rest_framework.routers import SimpleRouter
from .views import UserSpecializationProcedureMappingViewSet 


router = SimpleRouter()
router.register('', UserSpecializationProcedureMappingViewSet,)
urlpatterns = router.urls