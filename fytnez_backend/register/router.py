from rest_framework import routers
from fytnez_backend.register.views.hydric_consumption_view import HydricConsumptionView

from fytnez_backend.register.views.user_view import UserView
from fytnez_backend.register.views.achievement_view import AchievementView

router = routers.DefaultRouter()
router.register(r"users", UserView)
router.register(r"achievements", AchievementView)
router.register(r"hydric_consumption",HydricConsumptionView)