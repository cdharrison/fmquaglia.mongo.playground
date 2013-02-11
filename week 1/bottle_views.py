import bottle

@bottle.route('/')
def things():
	my_things = ['hammer', 'screw driver', 'saw']
	#return bottle.template('things', things=my_things, user='Fabricio')
	return bottle.template('things', 
		{
			'things':my_things, 
			'user':'Fabricio'
		}
	)

bottle.debug(True)
bottle.run(host='localhost', port="8089")