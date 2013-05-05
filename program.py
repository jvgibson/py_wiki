#! /usr/bin/env python
import sys
import urllib
import json


def showsome(searchfor):
    query = urllib.urlencode({'q': searchfor})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_response = urllib.urlopen(url)
    search_results = search_response.read()
    results = json.loads(search_results)
    data = results['responseData']
    print 'Total results: %s' % data['cursor']['estimatedResultCount']
    hits = data['results']
    print 'Top %d hits:' % len(hits)
    for h in hits: print ' ', h['url']
    print 'For more results, see %s' % data['cursor']['moreResultsUrl']


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
    except:
      print 'Invalid Input, Please try again'


  #check the pages for the top 20 most used words

  #print out the words and count

if __name__ == "__main__":
  sys.exit(main())

