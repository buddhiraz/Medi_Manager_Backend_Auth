from rest_framework.routers import SimpleRouter
from .views import ConsultationMedicineViewSet 


router = SimpleRouter()
router.register('', ConsultationMedicineViewSet)
urlpatterns = router.urls