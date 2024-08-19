A, B = map(int, input().split())
C = list(map(int, input().split()))

k = 0
sum = 0
cnt = 0

for i in range(A):
    sum += C[i]

    while sum >= B: # 하나만 뺐을 때 B보다 클수도 있으므로 while로 계속 빼줘야함
        if sum == B:
            cnt += 1
        sum -= C[k]
        k += 1

print(cnt)