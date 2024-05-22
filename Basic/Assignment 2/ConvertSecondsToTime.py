##### Mohammad Ali Mirzaei #####

Seconds = int(input("Enter the seconds : "))
Hours = Seconds // 3600
Minutes = (Seconds % 3600) // 60
Seconds = Seconds % 60

print(f"Result : {int(Hours)}:{int(Minutes)}:{int(Seconds)}")