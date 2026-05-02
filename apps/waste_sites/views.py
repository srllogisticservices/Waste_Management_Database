from django.http import JsonResponse


def health(request):
    return JsonResponse({"app": "waste_sites", "status": "ok"})
