N = int(input())
P = list(map(int, input().split()))
P.insert(0,0)
dp = [0] * (N+1)

for i in range(1,N+1):
    for j in range(1, i+1):
        # 반복하면서 그 전거와 1번 / 그 전전거와 2 더한거 쭉 반복복
        dp[i] = max(dp[i], P[j] + dp[i-j])

print(dp[N])