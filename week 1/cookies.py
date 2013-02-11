import bottle

@bottle.route('/')
def root_page():
	cookies = ['oreos', 'melbas', 'chocochips', 'crackers']
	return bottle.template('cookies',
		{
			'cookies': cookies
		}
	)

@bottle.post('/set_cookie')
def form_confirmation():
	cookie = bottle.request.forms.get('cookie')
	if(cookie == None or cookie == ""):
		cookie = "None selected"
	bottle.response.set_cookie("cookie", cookie)
	bottle.redirect("/my_cookie")

@bottle.route('/my_cookie')
def show_cookie():
	cookie = bottle.request.get_cookie("cookie")
	return bottle.template('show_cookie', 
		{
			'cookie': cookie
		}
	)

bottle.debug(True)

bottle.run(host="localhost", port="8089")
