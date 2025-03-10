from django.http import HttpResponse
import re
from api.jwt import verify_token

class AuthenticationMiddleware:
    """Middleware responsable to authenticate user and check user permissions

    Returns:
        response: HttpResponse
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.excluded_paths = [
            re.compile(r"^/static"),
            re.compile(r"^/swagger"), 
        ]

    def __call__(self, request):
        if not any(pattern.match(request.path) for pattern in self.excluded_paths):
            # get token from header
            token = request.META.get('HTTP_AUTHORIZATION')

            if not token:
                return HttpResponse('unauthorized', status=401)

            # clean header to extract only token
            token = token.split(" ")[1]

            # check if token is valid and returns token properties
            decoded_token = verify_token(token)

            if not decoded_token:
                return HttpResponse('unauthorized', status=401)

            # add permissions to user session
            request.session['permissions'] = decoded_token['permissions']
        response = self.get_response(request)
        return response
