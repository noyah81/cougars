import json

# some dictionaries
p1 = { "name":"Calvin", "age":"17", "city":"San Diego", "Food":"Taco"}
p2 = { "name":"Jake", "age":"100", "city":"San Diego", "Food":"Orange"}
p3 = { "name":"Jill", "age":"16", "city":"Aspen", "Food":"Apple"}
p4 = { "name":"Bee", "age":"16", "city":"San Francisco", "Food":"Pear"}
p5 = {"name":"Spider", "age":"0", "city":"San Jose", "Food":"Grape"}

# a list of dictionaries
list_of_family = [p1, p2, p3, p4,p5]

# write some code to Print List of people one by one
#print("List of people")
#print(type(list_of_family))
#print(list_of_family)
#for person in list_of_family:
#print(person['name'] + "," + str(person['age']) + "," + person['city'])
#print()



# turn list to dictionary of people in a family
family = {'family': list_of_family}
print("Dictionary of member")
List = family["family"]
for member in List:
    print("age" + ": " + member["age"] + " ,name" + ": " + member["name"] + " ,city" + ": " + member["city"]+ " ,food" + ": " + member["Food"]  )
    #print(members["name"] + " , " + members["age"]+ " , " + members["city"]+ " , " + members["Food"])

# write some code to Print People from Dictionary




# turn dictionary to JSON (aka string)
json_people = json.dumps(list_of_family)
print("Dictionary to JSON")
for char in json_people:
    print(char,end="!")
# write some code to print a space between each character of JSON
# hint use print(char, end ="-")
# INSERT CODE HERE




# turn dictionary to JSON, this can be sent via a browser
# write some code to unwind JSON using json.loads and print the people
# INSERT CODE HERE
print("JSON to Python")
print("JSON to Python")
PythonList = {"family": json.loads(json_people)}
NewList = {"Grandparents":[PythonList["family"][3],PythonList["family"][4]], "Parents":[PythonList["family"][1],PythonList["family"][2]]}
print(NewList)

for people in PythonList["family"]:
    print(people['name'] + "," + str(people['age']) + "," + people['city'])
print()
