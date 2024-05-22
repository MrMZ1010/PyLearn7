# MohammadAli Mirzaei

import random
marry = []

boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]

while len(boys)>0:
    random_boy = random.choice(boys)
    random_girl = random.choice(girls)

    marry.append((random_boy, random_girl))
    
    boys.remove(random_boy)
    girls.remove(random_girl)

print((marry))

