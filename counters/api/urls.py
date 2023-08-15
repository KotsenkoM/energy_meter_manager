from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from .views import EnergyMeterViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('counters', EnergyMeterViewSet, basename='counters')

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1',
        description='API для опроса приборов учета электроэнергии'
    ),
    public=True,
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
