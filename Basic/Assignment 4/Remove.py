##### Mohammad Ali Mirzaei #####

Number = int(input("Enter the length of the list : "))
lst = []

for i in range(Number):
    lst.append(int(input(f"Enter number {i+1} : ")))

for number in lst :
    if lst.count(number) > 1 :
        lst.remove(number)
print(lst)
