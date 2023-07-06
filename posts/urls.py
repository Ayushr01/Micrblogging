from django.urls import path
from rest_framework import routers
from posts import views as posts_views

router = routers.SimpleRouter()
router.register("", posts_views.PostViewSet)

urlpatterns = router.urls