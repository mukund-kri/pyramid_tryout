'''
All the views related to auth are here.
'''

from pyramid.view import view_config, forbidden_view_config
from pyramid.security import authenticated_userid
from pyramid.exceptions import HTTPForbidden


@view_config(route_name='home', renderer='index.mak')
def my_view(request):
    
    if not authenticated_userid(request):
        raise HTTPForbidden()
    
    return {'project': 'zurb_simple'}


@forbidden_view_config(renderer='login.mak')
@view_config(route_name='login', renderer='login.mak')
def login(request):
    
    return {}