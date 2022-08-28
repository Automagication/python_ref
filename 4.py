"""




STRING

lower()
upper()
strip()
title()
split()
find()
replace()
"".join()



"""
from cgitb import text


game = "Popular Nintendo Game: Mario Kart"

# print("l" in game)
# print("x" in game)

color="yellow"
# print(color[-1])
# print(color[4:6])

for c in color:
    pass
    # print(c)
    
colors=["red","blue","purple"]    
    
print(len(colors))

x="iam str1"
y="Iam str2"
print(x+" "+y)

fruit="grape"
# ind=fruit[5]
# print(ind)

msg1 = 'Fred scored {} out of {} points.'
msg1=msg1.format(3, 10)
print(msg1)


greeting = "Welcome To Chili's"
print(greeting.lower())


text1="apples and oranges"
text2="....-...apples and oranges...+..."
print(text1)
print(text1.strip())
print(text2.strip('.+'))


my_var = "dark knight"
print(my_var.title()) 


text = "Silicon Valley"
print(text.split())
print(text.split('i'))


mountain_name = "Mount Kilimanjaro"
res=mountain_name.find('z')
print(res)


fruit = "Strawberry"
res=fruit.replace('r','R')
print(res)

res=""
dinosaur = "T-Rex"
res=dinosaur.upper()
print(res)



res=" ".join(["Codecademy", "is", "awesome"])
print(res)

