<h1>Task Listing</h1>

<table>	 
% for task in tasks:
  <tr>
    <td>${task.title}</td>
    <td><a href="/del/${task.id}">Delete</a></td>
  </tr>
% endfor 
</table>

<br/>
<div>
  <a href="/add">Add a new task</a>
</div>