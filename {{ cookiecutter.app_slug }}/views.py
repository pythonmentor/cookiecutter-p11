from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .helpers import get_favorites


@login_required
def export(request):
    """Exports favorites as a json file."""
    favorites = get_favorites()
    return JsonResponse(favorites, safe=False)
