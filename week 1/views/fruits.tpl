<html>
<head>
	<title>Available Fruits</title>
</head>
<body>
<h1>These are the available fruits</h1>
<ul>
%for fruit in fruits:
	<li>{{fruit}}</li>
%end
</ul>
<div>
<form method="POST" action="fruit_confirmation">
	<label>
		Select your favorite fruit: <input name="fruit" type="text" />
		<input type="submit" value="submit">
	</label>
</form>
</div>
</body>
</html>