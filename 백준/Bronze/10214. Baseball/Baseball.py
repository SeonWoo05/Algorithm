T = int(input())

for i in range(T):
    A,B = 0,0
    for i in range(9):
        a,b = 0,0
        a,b = map(int, input().split())
        A += a
        B += b   
    if A > B:
        print('Yonsei')
    elif A == B:
        print('Draw')
    elif A < B:
        print('Korea')