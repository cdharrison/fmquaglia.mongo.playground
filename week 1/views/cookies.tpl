<html>
<head>
	<title>Available Cookies</title>
</head>
<body>
<h1>These are the available cookies</h1>
<ul>
%for cookie in cookies:
	<li>{{cookie}}</li>
%end
</ul>
<div>
<form method="POST" action="/set_cookie">
	<label>
		Select your favorite cookie: <input name="cookie" type="text" />
		<input type="submit" value="submit">
	</label>
</form>
</div>
</body>
</html>