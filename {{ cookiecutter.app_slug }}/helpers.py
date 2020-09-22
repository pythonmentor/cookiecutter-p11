from django.apps import apps as django_apps
from django.conf import settings


def get_completions():
    """Returns a list of dictionaries containing the name suggestions for autocompletion."""
    model = get_model("{{ cookiecutter.app_slug.upper() }}_MODEL")
    field = getattr(settings, "{{ cookiecutter.app_slug.upper() }}_FIELD")
    if not isinstance(field, str):
        raise ImproperlyConfigured(
            f"{{ cookiecutter.app_slug.upper() }}_FIELD must be a string."
        )
    order = getattr(settings, "{{ cookiecutter.app_slug.upper() }}_ORDER", ['?'])
    if not isinstance(field, str):
        raise ImproperlyConfigured(
            f"{{ cookiecutter.app_slug.upper() }}_ORDER must be a list of strings."
        )
    return list(model.objects.order_by(*order).values_list(field, flat=True))

def get_model(self, constant_name):
    """Returns the model specified with constant_name in the settings."""
    model_name = getattr(settings, constant_name)
    try:
        return django_apps.get_model(model_name, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            f"{constant_name} must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            f"{constant_name} refers to model '{model_name}' "
            "that has not been installed"
        )
