from django.http import JsonResponse
from django.conf import settings

class MobileAppAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get('X-Api-Key')
        if request.path.startswith('/api/'):
            if api_key != settings.MOBILE_APP_SECRET_KEY:
                return JsonResponse({'error': 'Unauthorized'}, status=401)
        
        return self.get_response(request)