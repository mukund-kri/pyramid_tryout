from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from deform import Form, ValidationFailure

from pyramidme.models import Task
from pyramidme.forms import TaskSchema


@view_config(route_name='home', renderer='list.mak')
def listing(request):
    tasks = Task.objects
    return {'tasks': tasks}

@view_config(route_name='add', renderer='add.mak')
def add(request):
    schema = TaskSchema()
    form = Form(schema, buttons=('submit',))
    
    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = form.validate(controls)
            Task.add(appstruct)
        except ValidationFailure as e:
            return {'form': e.render()}
        else:
            return HTTPFound(request.route_url('home'))
    return {'form': form.render()}


@view_config(route_name='delete')
def delete(request):
    task_id = request.matchdict.get('id', None)
    Task.remove(task_id)
    return HTTPFound(request.route_url('home'))
