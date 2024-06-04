# Happy Number
def isHappyNum(n):
    visited = set()

    while True: # 무한루프 시작
        ret = 0
        for x in str(n):
            visited.add(int(x))
            ret += int(x)*int(x)
        
        if ret == 1:
            return True
        if ret in visited: # 방문했던 값중에 있으면 무한루프 반복되므로
            return False # False 반환하고 함수 종료
        n = ret # 반복

n = int(input())
result = isHappyNum(n)

if result == True:
    print('HAPPY')
else:
    print('UNHAPPY')