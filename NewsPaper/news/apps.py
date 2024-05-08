from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
<<<<<<< HEAD

    def ready(self):
        from . import signals
=======
>>>>>>> 17c9f21ccc6e4eff5df1ad86acbf84c87de46949
