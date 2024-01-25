from rest_framework.routers import SimpleRouter
from .views import ConsultationInstructionViewSet 


router = SimpleRouter()
router.register('', ConsultationInstructionViewSet)
urlpatterns = router.urls