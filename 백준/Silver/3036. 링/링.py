def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b) # 최대 공약수 구하는 함수

N = int(input())
rings = list(map(int, input().split()))

for i in range(1,N):
    t = gcd(rings[0],rings[i])
    print(f'{rings[0] // t}/{rings[i] // t}')