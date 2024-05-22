##### Mohammad Ali Mirzaei #####

import random

Number = int(input("Enter a number : "))
Numbers_List = []

for i in range(Number):
    if i not in Numbers_List :
        Numbers_List.append(random.randint(1,100))
print(Numbers_List)
