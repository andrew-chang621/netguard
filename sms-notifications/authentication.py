class AuthenticationMiddleWare(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print("something you want done in every http request")
        print(environ)
        return self.app(environ, start_response)
