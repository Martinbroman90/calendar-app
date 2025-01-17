from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet

# Skapa en router för API:et
router = DefaultRouter()
router.register(r'events', EventViewSet)

# Lägg till routen i URL-konfigurationen
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Här kopplar vi in API:et
]
