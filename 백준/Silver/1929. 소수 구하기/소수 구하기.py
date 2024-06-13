a,b = map(int, input().split())
for i in range(a,b+1):
    if i == 1: # 1은 소수가 아니므로 제거
        continue
    for j in range(2,int(i**(1/2))+1):
        if i % j == 0: # 자신의 양의 제곱근 이하의 배수만 다 제거
            break # 약수 있으면 바로 for문 탈출
    else:
        print(i)