'''
All the views related to auth are here.
'''

from pyramid.view import view_config, forbidden_view_config
from pyramid.security import authenticated_userid, remember
from pyramid.httpexceptions import HTTPForbidden, HTTPFound
from deform import ValidationFailure, Form

from .forms import LoginSchema
from auth_experiments.models import User


@view_config(route_name='home', renderer='index.mak')
def my_view(request):
    
    if not authenticated_userid(request):
        raise HTTPForbidden()
    
    return {'project': 'zurb_simple'}


@forbidden_view_config(renderer='login.mak')
@view_config(route_name='login', renderer='login.mak')
def login(request):
    
    schema = LoginSchema()
    form = Form(schema)

    if 'form.submitted' in request.params:
        controls = request.POST.items()
        try:
            form.validate(controls)
            user = request.params['email']
            password = request.params['password']
            if User.valid_user(user, password):
                headers = remember(request, 'mukund')
                return HTTPFound(location = '/',
                                 headers = headers)

        except ValidationFailure as e:
            return {'error': e.error.asdict()}

    return {'error': {}}
