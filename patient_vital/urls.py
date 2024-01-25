from rest_framework.routers import SimpleRouter
from .views import PatientVitalViewSet 


router = SimpleRouter()
router.register('', PatientVitalViewSet)
urlpatterns = router.urls