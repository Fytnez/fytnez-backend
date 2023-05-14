from rest_framework import routers

from fytnez_backend.register.views.user_view import UserView

router = routers.DefaultRouter()
router.register(r"users", UserView)
