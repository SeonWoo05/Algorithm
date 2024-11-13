def tree_by_level(K,values):
    def build_tree(level,start,end):
        if level >= K or start > end:
            return
        
        mid = (start + end) // 2
        levels[level].append(values[mid])

        build_tree(level+1,start,mid-1)
        build_tree(level+1,mid+1,end)

    levels = [[] for _ in range(K)]
    build_tree(0,0,len(values)-1)
    return levels

K = int(input())
values = list(map(int, input().split()))

result = tree_by_level(K,values)
for level in result:
    print(*level)