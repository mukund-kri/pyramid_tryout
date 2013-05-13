from pyramid.security import (
    Allow,
    Everyone,
    )

from .user import User

class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:editors', 'edit') ]
    def __init__(self, request):
        pass
