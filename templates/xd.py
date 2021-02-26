# code here
import json

# some dictionaries
p1 = {"name": "John", "age": 61, "city": "Eugene"}
p2 = {"name": "Megan", "age": 18, "city": "Taipei"}
p3 = {"name": "Ryan", "age": 16, "city": "Los Angeles"}
p4 = {"name": "Shekar", "age": 16, "city": "San Francisco"}
p5 = {"name": "Name", "age": 16, "city": "San Francisco"}
# a list of dictionaries
list_of_people = [p1, p2, p3, p4, p5]
# write some code to Print List of people one by one
print("List of people")
print(type(list_of_people))
print(list_of_people)
for person in list_of_people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()

# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("Dictionary of people")
print(type(dict_people))
print(dict_people)
# write some code to Print People from Dictionary


# turn dictionary to JSON (aka string)
json_people = json.dumps(list_of_people)


def print(param):
    pass


print("JSON People #1")
print(type(json_people))
print(json_people)
# write some code to print a space between each character of JSON
# hint use print(char, end ="-")
# INSERT CODE HERE
for char in json_people:
    print(char, end="+")

# turn dictionary to JSON, this can be sent via a browser
json_people = json.dumps(list_of_people)
# the result is a JSON file:
print("JSON People #2")
print(type(json_people))
print(json_people)
# write some code to unwind JSON using json.loads and print the people
# INSERT CODE HERE
x = json.loads(json_people)
print(x)