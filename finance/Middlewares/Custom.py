from django.http import Http404
URLS = ['/dashboard/']

class HRMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        user = request.user
        response = self.get_response(request)
        if not (user and user.is_authenticated and user.email) and request.path in URLS:
            raise Http404
        return response