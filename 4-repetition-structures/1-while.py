age = int(input())

compulsoryVoting = 0

while age < 18:
    compulsoryVoting += 1
    age += 1

print(f'{compulsoryVoting} years until compulsory voting')