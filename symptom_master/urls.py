from rest_framework.routers import SimpleRouter
from .views import SymptomMasterViewSet 


router = SimpleRouter()
router.register('', SymptomMasterViewSet,)
urlpatterns = router.urls