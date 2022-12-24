from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("studentview", StudentViewSet, basename="StudentViewSet")
router.register(
    "studentProfile",
    SPViewset,
    basename="SPViewset",
)
router.register("mentorview", MentorViewSet, basename="MentorViewSet")
router.register("parentInteraction", PIViewSet, basename="PIViewSet")
router.register("mentorGeneralRemarks", MGRViewSet, basename="MGRViewSet")
# router.register("academics", SAPViewSet, basename="SAPViewSet")
router.register("studentInteraction", SIViewSet, basename="SIViewSet")


urlpatterns = [
    path("", include(router.urls)),
]
# <str:pk>
