import string
import sys

# l=["harsha",777]

# l2=[x for x in l if x==777]
# print(l)


pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
for p in pat:
   pass
   if (p == 0):
       current = p
       break
   elif (p % 2 == 0):
       continue
   print(p)       # output => 1 3 1 3 1
print(current)    # output => 0
