from django.urls import include, path

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from events.views import EventsViewSet
from organisations.views import OrganisationsViewSet


router = SimpleRouter()
router.register(r'organisations', OrganisationsViewSet)
router.register(r'events', EventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]