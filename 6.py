"""




DICT




"""

my_dictionary = {"song": "Estranged", "artist": "Guns N' Roses"}
print(my_dictionary["song"])
my_dictionary["song"] = "Paradise City"
print(my_dictionary)

#***********************************update

dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}

dict1.update(dict2)
print(dict1)
#***********************************immutable key

dictionary1 = {
  1: 'hello', 
  'two': True, 
  '3': [1, 2, 3], 
  'Four': {'fun': 'addition'}, 
  5.0: 5.5,
  (1,2,3):"dsadas"
  
}

print(dictionary1)
#***********************************unordered item
my_dictionary = {1: "L.A. Lakers", 2: "Houston Rockets"}
print(my_dictionary)

#***********************************keys,values,items

ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}

ex1=ex_dict.keys()
# dict_keys(["a","b","c"])

ex2=ex_dict.values()
# dict_values(["anteater", "bumblebee", "cheetah"])

ex3=ex_dict.items()
# dict_items([("a","anteater"),("b","bumblebee"),("c","cheetah")])

print(ex_dict.keys())
print(ex_dict.values())
print(ex_dict.items())
#***********************************get()

# without default
n1={"name": "Victor"}.get("name")
# returns "Victor"

n2={"name": "Victor"}.get("nickname")
# returns None

# with default
n3={"name": "Victor"}.get("nickname", "nickname is not a key")
# returns "nickname is not a key"

print(n1)
print(n2)
print(n3)
#***********************************pop()

famous_museums = {'Washington': 'Smithsonian Institution', 'Paris': 'Le Louvre', 'Athens': 'The Acropolis Museum'}
famous_museums.pop('Athens')
print(famous_museums) # {'Washington': 'Smithsonian Institution', 'Paris': 'Le Louvre'}

