import urllib
import simplejson as json
import sys

def search_twitter(query='python'):
	url = 'http://search.twitter.com/search.json?show_user=true&q=' + query
	response = urllib.urlopen(url).read()
	data = json.loads(response)
	return data['results']
	
def print_tweets(tweets):
  for tweet in tweets:
    print tweet['text'] + '\n'

if __name__ == "__main__":
  query = sys.argv[1]
  results = search_twitter(query)
  print_tweets(results)

def search_user(query):
	url = 'http://search.twitter.com/search.json?showuser=true&q=' + query
	response = urllib.urlopen(url).read()
	data = json.loads(response)
	return data['results']
	
if __name__ == "__main__":
  query = sys.argv[1]
  results = search_user(query)
  print_tweets(results)