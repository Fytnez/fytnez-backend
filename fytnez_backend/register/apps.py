from django.apps import AppConfig


class CadastroConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fytnez_backend.register"

    def ready(self):
        import register
        import models
        import models.user
