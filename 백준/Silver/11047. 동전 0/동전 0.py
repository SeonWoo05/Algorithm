N, K = map(int, input().split())
A = []
for i in range(N):
    x = int(input())
    A.append(x)

A.sort(reverse=True)

cnt = 0

# for i in A:
#     while K >= i:
#         K -= i
#         cnt += 1 # 정답은 나오는데 시간초과 뜸 => while로 계속 반복하지말고 최대로 뺄 수 있는만큼 한번에 빼기

for i in A:
    if K == 0:
        break
    
    if K >= i:
        cnt += K // i
        K %= i
        
print(cnt) 