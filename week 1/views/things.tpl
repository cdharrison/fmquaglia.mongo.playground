<html>
<head>
	<title>These are my things</title>
</head>
<body>
<h1>
	My name is {{user}} and these are my things
</h1>
%for thing in things:
	<li>{{thing}}</li>
%end
</body>
</html>