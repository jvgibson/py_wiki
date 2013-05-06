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


def showsome(searchfor):  

    words = []
  
    query = urllib.urlencode({'q': searchfor})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_response = urllib.urlopen(url)
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
      
      # Print all of the paragraphs to screen
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
      
      #grabs the top sites on wikipedia
      userLocation = userLocation + ' site:wikipedia.org'
      showsome(userLocation)
    except Exception, e:
      print "FAIL: %s" % e

  #check the pages for the top 20 most used words

  #print out the words and count

if __name__ == "__main__":
  sys.exit(main())

