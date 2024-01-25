from rest_framework.routers import SimpleRouter
from .views import ConsultationSymptomViewSet 


router = SimpleRouter()
router.register('', ConsultationSymptomViewSet)
urlpatterns = router.urls