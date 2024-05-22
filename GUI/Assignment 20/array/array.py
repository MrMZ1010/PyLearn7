# MohammadAli Mirzaei

print(
    "Enter Numbers for check symetric array (put space between each number): 1 4 3 4 1 => [1,4,3,4,1]"
)
araye = input().split(" ")
araye_len = len(araye)
araye_half_index = araye_len // 2
pos = ''
less = -1
for num in range(0, araye_len - araye_half_index - 1):
    if araye[num] == araye[less]:
        pos = '🎉Array is symantic'
    else:
        pos = 'Array is not symantic'
    less-=1

print(pos)
