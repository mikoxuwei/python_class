import json

numbers = [10, 20, 30, 70, 191, 23]
filename = 'p0317/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f) # json.dump() function to store the set of numbers in numbers.json file

data = {
    'name': 'John',
    'Occupation': 'Doctor',
}
dict_1 = json.dumps(data) # json.dumps() function to convert the dictionary data into a JSON formatted string
print(dict_1)
# Output: {"name": "John"", "Occupation": "Doctor"}

with open('p0317/student.json', 'r') as f1:
    data = json.load(f1)
    print(data)


# people_string = '''
# {
#     "people": [
#         {
#             "name": "John Smith",
#             "phone": "615-555-7164",
#             "emails": ["johnsmith@gmail.com", "jsmith@hotmail.com"],
#             "has_license": false
#         },
#         {
#             "name": "Jane Doe",
#             "phone": "560-555-5153",
#             "emails": ["janedoe@gmail.com", "janeD@kmutnb.ac.th"],
#             "has_license": true
#         }
#     ]
# }
# '''
# # data = people_string
# data = json.loads(people_string)
# for person in data['people']:
#     print(person)

people_string = {
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@gmail.com", "jsmith@hotmail.com"],
            "has_license": False
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": ["janedoe@gmail.com", "janeD@kmutnb.ac.th"],
            "has_license": True
        }
    ]
}

# data = people_string
data = people_string
for person in data['people']:
    print(person)