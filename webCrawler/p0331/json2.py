import json
with open('d:/nutn_school/python_class/webCrawler/p0331/states.json', 'r') as f:
    data = json.load(f)
for state in data['states']:
    # print(state['name'], state['abbreviation'])
    del state['area_codes']
with open('d:/nutn_school/python_class/webCrawler/p0331/states2.json', 'w') as f:
    json.dump(data, f)