# N×N의 표에 수 N2개 채워져 있다. 채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다. N=5일 때의 예를 보자.
# 12	7	9	15	5
# 13	8	11	19	6
# 21	10	26	31	16
# 48	14	28	35	25
# 52	20	32	41	49
# 이러한 표가 주어졌을 때, N번째 큰 수를 찾는 프로그램을 작성하시오. 표에 채워진 수는 모두 다르다.
import sys
import heapq

read = lambda: sys.stdin.readline().rstrip()

n = int(read())
heap = []

for _ in range(n):
	nums = list(map(int, read().split()))

	if not heap:
		for num in nums:
			heapq.heappush(heap, num)
	else:
		for num in nums:
			if heap[0] < num:
				heapq.heappush(heap, num)
				heapq.heappop(heap)

print(heap[0])