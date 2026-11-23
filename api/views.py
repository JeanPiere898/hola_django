from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def hola(request):
    data = {
        "mensaje": "Hola Mundo",
        "lenguaje": "Python",
        "framework": "Django"
    }
    return JsonResponse(data)