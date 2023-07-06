from django.urls import path
from rest_framework import routers

from users import views as user_views

router = routers.SimpleRouter()
router.register("", user_views.UserViewSet)

urlpatterns = [
    path("", user_views.UserRegisterAPIView().as_view(http_method_names=['post']), name='register'), 
    path("login/", user_views.LoginAPIView().as_view(), name='login'),   
    path("logout/", user_views.LogoutAPIView().as_view(), name='logout'),
]

urlpatterns += router.urls