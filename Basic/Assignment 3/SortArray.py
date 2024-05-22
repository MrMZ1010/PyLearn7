##### Mohammad Ali Mirzaei #####

Number = int(input("Enter the length of your list : "))
Numbers_List = []

for i in range(Number) : 
    Numbers_List.append(int(input(f"Enther the number {i + 1} : ")))

if Numbers_List == sorted(Numbers_List) :
    print("Your list is sorted ")
else :
    print("Your list is not sorted")
