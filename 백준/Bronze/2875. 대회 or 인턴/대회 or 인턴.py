A,B,C = map(int, input().split())

team = 0

while True:
    A -= 2
    B -= 1
    if A < 0 or B < 0 or A+B < C:
        break
    team += 1

print(team)