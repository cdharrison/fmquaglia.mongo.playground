import bottle

@bottle.route('/')
def root_page():
	return "Hello Word"

@bottle.route('/testpage')
def test_page():
	return "This is a test page"

bottle.debug(True)
bottle.run(host='localhost', port=8082)