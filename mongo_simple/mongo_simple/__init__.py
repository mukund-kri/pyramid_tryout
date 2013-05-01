from urllib.parse import urlparse

from pyramid.config import Configurator
import pymongo


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)

    db_url = urlparse(settings['mongo_uri'])
    config.registry.db = pymongo.Connection(
       host=db_url.hostname,
    )
    
    def get_db(request):
        db = config.registry.db[db_url.path[1:]]
        return db
        
    config.add_request_method(get_db, 'db', reify=True)    
    
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
