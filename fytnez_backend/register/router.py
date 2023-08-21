from django.urls import path, re_path
from rest_framework import routers
from fytnez_backend.register.views.user_view import UserView

router = routers.DefaultRouter()
router.register(r"users", UserView)


urlpatterns = [
    path('login/', UserView.login, name='login'),
    re_path(r'^minha_view_protegida/$', UserView.minha_view_protegida, name='minha_view_protegida'),
]

urlpatterns += router.urls