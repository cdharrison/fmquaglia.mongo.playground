require "rubygems"
require "sinatra"


configure do
  require "mongo"
  connection = Mongo::Connection.new
  database = connection['test']
  names = database['names']
  get '/' do
    name = names.find_one.to_hash['name']
    "<p>Hola #{name}</p>"  
      
  end  
end