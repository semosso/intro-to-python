# program that finds what given site looked like on specific date, and then opens it
import webbrowser # imports the whole library
import json
from urllib.request import urlopen # unlike ln 2, imports only specific function from library

print('Let\'s find an old wesbite.')
site = input('Type a website URL: ')
era = input('Type a year, month, and day, in YYYYMMDD format: ')
url = 'http://archive.org/wayback/available?url=%s&timestamp=%s' % (site, era) # interessante o que isso faz
response = urlopen(url)
contents = response.read()
text = contents.decode('utf-8')
data = json.loads(text)
try:
    old_site = data['archived_snapshots']['closest']['url']
    print('Found this copy: ', old_site)
    print('It sould appear in your browser now.')
    webbrowser.open(old_site)
except:
    print('Sorry, no luck finding', site)

# Same as above but now using the external Python software packaged called REQUESTS
import webbrowser
import requests # had to install it via pip first

print('Let\'s find an old wesbite.')
site = input('Type a website URL: ')
era = input('Type a year, month, and day, in YYYYMMDD format: ')
url = 'http://archive.org/wayback/available?url=%s&timestamp=%s' % (site, era) # interessante isso aqui
response = requests.get(url)
data = response.json()
try:
    old_site = data['archived_snapshots']['closest']['url']
    print('Found this copy: ', old_site)
    print('It sould appear in your browser now.')
    webbrowser.open(old_site)
except:
    print('Sorry, no luck finding', site)