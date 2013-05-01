from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    print(request.db)
    return {'project': 'mongo_simple'}
