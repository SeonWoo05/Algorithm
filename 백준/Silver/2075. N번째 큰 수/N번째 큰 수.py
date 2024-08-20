import heapq

n = int(input())
min_heap = []

for i in range(n):
	num_list = list(map(int, input().split()))
	if not min_heap: # min_heap에 아무것도 없는 첫번째 입력 시
		for num in num_list:
			heapq.heappush(min_heap, num) # min_heap 채우기
	else:
		for num in num_list: # min_heap에 값이 있을 시 길이를 n으로 유지하기
			if min_heap[0] < num: # min_heap 최솟값보다 현재 숫자가 클 경우 n번째로 큰 수가 바뀌어야 하기 때문에
				heapq.heappush(min_heap, num) # 현재 숫자를 push 하고
				heapq.heappop(min_heap) # 기존 최솟값 pop

print(min_heap[0])