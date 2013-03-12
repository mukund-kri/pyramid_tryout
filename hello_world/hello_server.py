from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='hello')
def hello(request):
    return Response("Hello Pyramid")

if __name__ == '__main__':
    config = Configurator()
    config.scan()
    
    config.add_route('hello', '/')
    
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

