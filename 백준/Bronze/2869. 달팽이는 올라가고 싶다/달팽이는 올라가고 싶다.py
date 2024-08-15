import math

A, B, V = map(int, input().split())

# 목표 지점에 도달하기 전까지 남은 거리를 (A-B)로 나누어 몇 일이 걸리는지 계산
# 마지막 날에는 미끄러지지 않으므로 A만큼 이동한 후 목표에 도달
days = math.ceil((V - B) / (A - B))

print(days)