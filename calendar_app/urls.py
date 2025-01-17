from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet

def home(request):
    return HttpResponse("Welcome to the Calendar App")

# Skapa en router för API:et
router = DefaultRouter()
router.register(r'events', EventViewSet)

# Lägg till routen i URL-konfigurationen
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Här kopplar vi in API:et
    path('', home),  # Lägg till denna rad för att hantera rot-URL:en
]
