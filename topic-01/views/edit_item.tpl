<html>
<body>
Editing item:
<hr/>
<form action="/edit/{{id}}" method="post">
    <p> Edit the item:<input name="description" value="{{description}}"></p>
    <p> <button type="submit">Submit</button></p>
</form>
<a href="/list"> cancel</a>
</body>
</html>