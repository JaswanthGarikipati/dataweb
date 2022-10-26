<html>
<body>
<table>
% for item in shopping_list:
<tr>
    <td>{{str(item['id'])}}</td>
    <td>{{str(item['desc'])}}</td>
    <td><a href="/edit/{{str(item['id'])}}">EDIT</a></td>
    <td><a href="/delete/{{str(item['id'])}}">DELETE</a></td>
</tr>
% end
</table>
<hr/>
<form action="/add" method="post">
    <p>New Item: <input name="description"/></p>
    <p><button type="submit">Submit</button>
</forms>
<hr/>
<a href="/add"> Add new item</a>
</body>
</html>
