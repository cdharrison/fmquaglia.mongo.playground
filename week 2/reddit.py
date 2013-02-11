import json
import pymongo
import urllib2

connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.reddit
stories = db.stories

reddit_science = urllib2.urlopen("http://www.reddit.com/r/science.json")
reddit_home = urllib2.urlopen("http://www.reddit.com/.json")

parsed = json.loads(reddit_home.read())

for item in parsed['data']['children']:
	inserted = item['data']
	stories.insert(inserted)
	print inserted

parsed = json.loads(reddit_science.read())

for item in parsed['data']['children']:
	inserted = item['data']
	stories.insert(inserted)
	print inserted
