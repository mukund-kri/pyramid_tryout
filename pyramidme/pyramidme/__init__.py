from urllib.parse import urlparse

from pyramid.config import Configurator
from mongoengine import connect


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    url_str = settings.get('mongo_uri', 'mongodb://user:password@localhost:27012/default')
    url = urlparse(url_str)
    
    # TODO: Assert the url scheme is mongodb
    connect(url.path[1:])

    # TODO: Default values of host, port, username and password from mongo_uri parameter

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('add', '/add')
    config.add_route('delete', '/del/{id}')

    config.scan()
    return config.make_wsgi_app()
