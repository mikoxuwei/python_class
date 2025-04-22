import json
from urllib.request import urlopen
with urlopen('http://api.plos.org/search?q=title:DNA') as response:
    source = response.read()
# print(source)

data = json.loads(source)
# print(json.dumps(data, indent=2))
# print(len(data['response']['docs']))
for item in data['response']['docs']:
    name = item['title_display']
    title = item['title_display']
    # author = item['author_display']
    # journal = item['journal']
    print(name, title)