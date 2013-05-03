<h1>Task List</h1>

<table>
% for task in tasks:
	<tr>
		<td>${task['task']}</td>
		<td><a href="${request.route_url('tdelete', id=task['_id'])}">Delete</a></td>
		<td><a href="${request.route_url('tedit', id=task['_id'])}">Edit</a></td>
	</tr>
% endfor
</table>

<h2>Actions</h2>
<ul>
    <li><a href="${request.route_url('tadd')}">Add new Task</a></li>
</ul>
