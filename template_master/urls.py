from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TemplateMasterViewSet 


router = SimpleRouter()
router.register('', TemplateMasterViewSet,)
urlpatterns = router.urls