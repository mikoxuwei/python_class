# web connection
import urllib.request as ur
# open the src
src = 'https://www.nutn.edu.tw/'
with ur.urlopen(src) as response:
    data = response.read().decode('utf-8') # get original codes from the website(HTML, CSS, JS)
    print(data)