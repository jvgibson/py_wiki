#! /usr/bin/env python
import sys


def checkInput(city, state):

  if city.lower() in open('usCities.txt').read().lower() and state.lower() in open('usStates.txt').read().lower():
    return True
  else:
    return False

#Main function
def main(argc=None):
  #get the users input
  
  check = False

  while(not check):
    try:

      userLocation = raw_input('Enter a US City and State (such as "Seattle, WA"): ')
      uCity, uState = userLocation.split(",")
      check = checkInput(uCity.strip(),uState.strip())
      print userLocation
    except:
      print 'Invalid Input, Please try again'
  #check the users input

  #ckeck wiki api for search words in a city

  #check the pages for the top 20 most used words

  #print out the words and count

if __name__ == "__main__":
  sys.exit(main())

