from pyramid.config import Configurator

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from auth_experiments.models import User


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    
    # Auth --------------------------------------------------------------------
    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', 
        hashalg='sha512', 
        callback=User.user_group)
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings,
                          root_factory='auth_experiments.models.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    
    # DB ----------------------------------------------------------------------
    db_url = urlparse(settings['mongo_uri'])
    config.registry.db = pymongo.Connection(
       host=db_url.hostname,
    )
    
    def get_db(request):
        db = config.registry.db[db_url.path[1:]]
        return db
        
    config.add_request_method(get_db, 'db', reify=True) 

    # Routes -----------------------------------------------------------------
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    config.scan()
    return config.make_wsgi_app()
