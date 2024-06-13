N = input()
arr = []
cnt = 0

for i in range(len(N)):
    if N[i] == "(":
        arr.append(i)

    else:
        if N[i-1] == "(":
            arr.pop()
            cnt += len(arr)
        else:
            arr.pop()
            cnt += 1
print(cnt)