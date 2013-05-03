from pyramid.view import view_config
from deform import Form
from deform import ValidationFailure
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.url import route_url
from bson.objectid import ObjectId

from .forms import TaskSchema


@view_config(route_name='tlist', renderer='list.mak')
def task_list(request):
    tasks = request.db['tasks'].find()      # Get all tasks
    return {'tasks': tasks}

@view_config(route_name='tadd', renderer='add.mak')
def task_add(request):
    schema = TaskSchema()
    form = Form(schema, buttons=('submit',))
    
    if 'submit' in request.POST:
        controls = request.POST.items()        
        try:
            appstruct = form.validate(controls)
            request.db['tasks'].save(appstruct)
        except ValidationFaliure as e:
            return {'form': e.render()}
        else:
            return HTTPFound(route_url('tlist', request))
    return {'form': form.render()}

@view_config(route_name='tdelete')
def task_delete(request):
    id = request.matchdict.get('id', None)
    if id:
        request.db['tasks'].remove({'_id': ObjectId(id)})
    return HTTPFound(route_url('tlist', request))

@view_config(route_name='tedit', renderer='edit.mak')
def task_edit(request):
    schema = TaskSchema()
    form = Form(schema, buttons=('submit',))
    
    if 'submit' in request.POST:
        controls = request.POST.items()        
        try:
            appstruct = form.validate(controls)
            request.db['tasks'].save(appstruct)
        except ValidationFaliure as e:
            return {'form': e.render()}
        else:
            return HTTPFound(route_url('tlist', request))
    return {'form': form.render()}
