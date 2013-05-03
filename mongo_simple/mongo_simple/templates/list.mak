<h1>Task List</h1>

<table>
% for task in tasks:
	<tr>
		<td>${task['task']}</td>
		<td><a href="${request.route_url('tdelete', id=task['_id'])}">Delete</a></td>
	</tr>
% endfor
</table>
