import bottle

@bottle.route('/')
def root_page():
	fruits = ['orange', 'peach', 'pear', 'banana']
	return bottle.template('fruits',
		{
			'fruits': fruits
		}
	)

@bottle.post('/fruit_confirmation')
def form_confirmation():
	fruit = bottle.request.forms.get('fruit')
	if(fruit == None or fruit == ""):
		fruit = "None selected"

	return bottle.template('fruit_confirmation', 
		{
			'fruit': fruit
		}
	)

bottle.debug(True)

bottle.run(host="localhost", port="8089")
