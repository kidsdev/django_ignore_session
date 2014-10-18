from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.middleware import AuthenticationMiddleware, SessionAuthenticationMiddleware
from django.contrib.messages.middleware import MessageMiddleware

SESSION_IGNORE = ['/api/', '/pattie/']

class MySessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        request.IGNORE_SESSION = False
        for ignore in SESSION_IGNORE:
            if request.path_info.find(ignore) == 0:
                request.IGNORE_SESSION = True
                return
        super(MySessionMiddleware, self).process_request(request)

    def process_response(self, request, response):
        if request.IGNORE_SESSION:
            return response
        return super(MySessionMiddleware, self).process_response(request, response)

class MyAuthenticationMiddleware(AuthenticationMiddleware):
    def process_request(self, request):
        if request.IGNORE_SESSION:
            return
        super(MyAuthenticationMiddleware, self).process_request(request)

class MySessionAuthenticationMiddleware(SessionAuthenticationMiddleware):
    def process_request(self, request):
        if request.IGNORE_SESSION:
            return
        super(MySessionAuthenticationMiddleware, self).process_request(request)

class MyMessageMiddleware(MessageMiddleware):
    def process_request(self, request):
        if request.IGNORE_SESSION:
            return
        super(MyMessageMiddleware, self).process_request(request)

    def process_response(self, request, response):
        if request.IGNORE_SESSION:
            return response
        return super(MyMessageMiddleware, self).process_response(request, response)
