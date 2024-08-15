A,B,V = map(int, input().split())

days = (V-B) // (A-B) # 올라가서 도착하면 끝 => V-B
if ((V-B) % (A-B)) != 0:
    days += 1

print(days)