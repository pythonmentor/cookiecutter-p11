"""Configuration module for the FavoriteCart app."""

from django.apps import AppConfig


class {{ cookiecutter.app_slug.title }}Config(AppConfig):
    """Main config data structure for the {{ cookiecutter.app_slug }} app."""

    name = '{{ cookiecutter.app_slug }}'

    def ready(self):
        """Initializations to be performed with the app is ready."""
        try:
            from . import signals
        except ImportError:
            pass
