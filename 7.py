"""




FILES




"""


with open('somefile.txt') as file_object:
    print(file_object.readline())
    print(file_object.readline())
    file_object.close()
print('*********************************************')
import json

with open("somefile.json") as json_object:
    py_dict=json.load(json_object)
    print(py_dict)
    json_object.close()
print('*********************************************')
with open("somefile.txt",'a') as shop:
    shop.write('Tomato,brinjal\n')
    
with open("somefile.txt",'r') as shop:
    print(shop.read())
print('*********************************************')
with open('dairy.txt','w') as dairy:
    dairy.write('Special events for today')
    dairy.close()
    
with open("dairy.txt",'r') as dairy:
    print(dairy.read())
print('*********************************************')
with open('lines.txt') as file_object:
    file_data=file_object.readlines()
    for line in file_data:
        print(line)
    # print(file_data[0])
print('*********************************************')

    