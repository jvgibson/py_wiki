#! /usr/bin/env python
import sys
import urllib
import urllib2
import json
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re
from collections import Counter


def cleanHtmlRegex(i):
  i = str(i)
  regexPatClean = re.compile(r'<[^<]*?/?>')
  i = regexPatClean.sub('', i)
  i = re.sub('&\w+;','',i)
  return i


def topWords(searchfor):  
    
    #array for all the words on the page
    words = []
  
    #creates a google search on wikipedia with the city and state
    query = urllib.urlencode({'q': searchfor})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    request = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0"})
    search_response = urllib2.urlopen(request)
    
    #gets all the search results
    search_results = search_response.read()
    results = json.loads(search_results)
    data = results['responseData']
    hits = data['results']


    for h in hits:
      #Copy all of the content from the provided web page
      webpage = urlopen(h['url']).read()
      
      #Pass the article to the Beautiful Soup Module
      soup = BeautifulSoup(webpage)
      
      #Tell Beautiful Soup to locate all of the p tags and store them in a list
      paragList = soup.findAll('div')
     
      #puts all the words into an array
      for i in paragList: 
          i = cleanHtmlRegex(i)
          words = words + i.split()
    
    counter = Counter()
    for word in words:
      counter[word] += 1

    print counter.most_common(20)



def checkInput(city, state):

  if city.lower() in open('usCities.txt').read().lower() and state.lower() in open('usStates.txt').read().lower():
    return True
  else:
    return False

#Main function
def main(argc=None):
  
  check = False

  while(not check):
    try:
           
      #get the users input
      userLocation = raw_input('Enter a US City and State (such as "Seattle, WA"): ')

      #seperates the city and state
      uCity, uState = userLocation.split(",")
      
      #check the users input
      check = checkInput(uCity.strip(),uState.strip())
      
      #grabs the top sites on wikipedia and prints out the top 20 most used words
      userLocation = userLocation + ' site:wikipedia.org'
      topWords(userLocation)
    except Exception, e:
      print "FAIL: %s" % e


if __name__ == "__main__":
  sys.exit(main())

