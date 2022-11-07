<html>
<body>
<h2>Shopping list for <b>PEEWEE</b></h2>
<hr/>
<table>
% for item in shopping_list:
  <tr>
    <td>{{str(item['description'])}}</td>
    <td><a href="/edit/{{str(item['id'])}}">EDIT</a></td>
    <td><a href="/delete/{{str(item['id'])}}">DELETE</a></td>
  </tr>
% end
</table>
<hr/>
<form action="/add" method="post">
  <p>New item: <input name="description"/></p>
  <p><button type="submit">Submit</button>
</form>
</body>
</html>