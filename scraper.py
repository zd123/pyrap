import requests
from bs4 import BeautifulSoup

agent  = 'DataWrangling/1.1 (http://zipfianacademy.com; '
agent += 'class@zipfianacademy.com)'
headers = {'user_agent': agent}

url = 'http://www.azlyrics.com/l/lilwayne.html'
# Wrap in a try-except to prevent a maxTry connection error from erroring
# out the program. Return None if there are any issues.
try:
    r = requests.get(url, headers=headers)
except:
    print "error"

# Just in case there was a normal error returned. Pass back None.
if r.status_code != 200:
    print "error"

# Otherwise return a soupified object containing the url text encoded in
# utf-8. Will toss back errors on some pages without the encoding in place.
soup = BeautifulSoup(r.text.encode('utf-8'))

songs = soup.find("div", id="listAlbum").get_text()
song_titles = []
songs = songs.split("\n")
print songs
