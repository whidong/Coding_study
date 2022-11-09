import random, timeit

def quick_sort(A, first, last):#quick+insertion 분할중간중간
	global Qc, Qs
	if first >= last:
		Qc += 1
		return
	p = A[first]
	left, right = first +1, last
	while left <= right:
		Qc += 1
		while left <= last and A[left] < p:
			Qc += 2
			left += 1
		while right > first and A[right] >= p:
			Qc += 2
			right -= 1
		if left <= right:
			A[left], A[right] = A[right], A[left]
			left, right = left + 1, right - 1
			Qs += 1
	A[first], A[right] = A[right], A[first]
	Qs += 1
	if right-1 - first <= 10:
		insertion_sort(A,first, right)
	else:
		quick_sort(A, first,right)
	if last - left <= 10:
		insertion_sort(A,left,last)
	else:
		quick_sort(A, left, last)

def insertion_sort(A, s ,n):
	global Qc, Qs
	for i in range(s, n):
		j = i-1
		while j >= 0 and A[j] > A[j+1]:
			A[j], A[j+1] = A[j+1], A[j]
			Qc, Qs = Qc +1, Qs +1
			j= j-1
		Qc += 1

def quick_sort1(A, first, last):# 오리지날 quicksort
	global Q1c, Q1s
	if first >= last:
		Q1c += 1
		return
	p = A[first]
	left, right = first +1, last
	while left <= right:
		while left <= last and A[left] < p:
			Q1c += 1
			left += 1
		while right > first and A[right] >= p:
			Q1c += 1
			right -= 1
		if left <= right:
			A[left], A[right] = A[right], A[left]
			left, right = left + 1, right - 1
			Q1s += 1
	A[first], A[right] = A[right], A[first]
	Q1s += 1
	quick_sort1(A, first,right-1)
	if left >= last:
		return
	quick_sort1(A, left, last)

def quick_sort2(A, first, last): #quick sort + insertion sort 2번방법
	global Q2c, Q2s
	if first >= last:
		Q2c += 1
		return
	p = A[first]
	left, right = first +1, last
	while left <= right:
		while left <= last and A[left] < p:
			Q2c += 1
			left += 1
		while right > first and A[right] >= p:
			Q2c += 1
			right -= 1
		if left <= right:
			A[left], A[right] = A[right], A[left]
			left, right = left + 1, right - 1
			Q2s += 1
	A[first], A[right] = A[right], A[first]
	Q2s += 1
	if right-1 - first <= 10:
		return
	else:
		quick_sort2(A, first,right)
	if last - left <= 10:
		return
	else:
		quick_sort2(A, left, last)
	insertion_sort2(A,first,last)

def insertion_sort2(A, s ,n):
	global Q2c, Q2s
	for i in range(s, n):
		j = i-1
		while j >= 0 and A[j] > A[j+1]:
			A[j], A[j+1] = A[j+1], A[j]
			Q2c, Q2s = Q2c +1, Q2s +1
			j= j-1
		Q2c += 1


def merge_sort(A, first, last):
	global Ms, Mc
	if first >= last: return
	middle = (first+last)//2
	merge_sort(A, first, middle)
	merge_sort(A, middle+1, last)
	B = []
	i = first
	j = middle+1
	while i <= middle and j <= last:
		if A[i] <= A[j]:
			Mc, Ms = Mc + 1, Ms + 1
			B.append(A[i])
			i += 1
		else:
			Mc, Ms = Mc + 1, Ms + 1
			B.append(A[j])
			j += 1
	for i in range(i, middle+1): 
		Ms = Ms + 1
		B.append(A[i])
	for j in range(j, last+1): 
		Ms = Ms + 1
		B.append(A[j])
	for k in range(first, last+1): 
		A[k] = B[k-first]
		Ms = Ms + 1

def merge_sort_threeway(A, first, last):
	global M1s, M1c
	if first >= last: return
	to = (last-first)//3
	tw = 2*(last-first)//3
	merge_sort_threeway(A, first, first+to)
	merge_sort_threeway(A, first+to+1,first+tw)
	merge_sort_threeway(A, first+tw+1, last)
	B = []
	i = first
	j = first+to+1
	k = first+tw+1
	while i <= first+to and j <= first+tw or k <= last and j <= first+tw or k <= last and i <= first+to:
		if k == last+1:
			if A[i] <= A[j] and i <= first+to:
				B.append(A[i])
				i += 1
				M1c, M1s = M1c + 1, M1s + 1
			elif A[j] <= A[i] and j <= first+tw:
				B.append(A[j])
				j += 1
				M1c, M1s = M1c + 1, M1s + 1
		elif j == first+tw +1:
			if A[i] <= A[k] and i <= first+to:
				B.append(A[i])
				i += 1
				M1c, M1s = M1c + 1, M1s + 1
			elif A[k] <= A[i]  and k <= last:
				B.append(A[k])
				k += 1
				M1c, M1s = M1c + 1, M1s + 1
		elif i == first+to +1:
			if A[j] <= A[k]  and j <= first+tw:
				B.append(A[j])
				j += 1
				M1c, M1s = M1c + 1, M1s + 1
			elif A[k] <= A[j]  and k <= last:
				B.append(A[k])
				k += 1
				M1c, M1s = M1c + 1, M1s + 1
		else:
			if A[i] <= A[j] and A[i] <= A[k] and i <= first+to:
				B.append(A[i])
				i += 1
				M1c, M1s = M1c + 2, M1s + 1
			elif A[j] <= A[i] and A[j] <= A[k]  and j <= first+tw:
				B.append(A[j])
				j += 1
				M1c, M1s = M1c + 2, M1s + 1
			elif A[k] <= A[i] and A[k] <= A[j]  and k <= last:
				B.append(A[k])
				k += 1
				M1c, M1s = M1c + 2, M1s + 1
	for i in range(i, first+to+1): 
		B.append(A[i])
		M1s += 1
	for j in range(j, first+tw+1): 
		B.append(A[j])
		M1s += 1
	for k in range(k, last+1): 
		B.append(A[k])
		M1s += 1
	for z in range(first, last+1): 
		A[z] = B[z-first]	
		M1s += 1


def heap_sort(A):
	global Hc, Hs
	n = len(A)
	for k in range(n-1, -1, -1): 
		heapify_down(A, k, n)
	for k in range(len(A)-1, -1, -1):
		A[0],A[k] = A[k],A[0]
		Hs += 1
		n = n - 1 
		heapify_down(A, 0, n)

def heapify_down(A, k, n):
	global Hc, Hs
	while 2*k+1 < n: 
		L, R = 2*k + 1, 2*k + 2 
		if L < n and A[L] > A[k]:
			Hc += 1
			m = L
		else:
			Hc += 1
			m = k
		if R < n and A[R] > A[m]:
			Hc += 1
			m = R
		if m != k: 
			A[k], A[m] = A[m], A[k]
			k = m
			Hs += 1
		else: break
##
## 여기에 세 가지 정렬함수를 위한 코드를...
##


# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
Q1c,Q1s,Q2c,Q2s,M1c,M1s =0,0,0,0,0,0
n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]
D = A[:]
E = A[:]
F = A[:]

print("")
print("Quick sort1:")
print("time =", timeit.timeit("quick_sort1(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Q1c, Q1s))
print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Quick sort2:")
print("time =", timeit.timeit("quick_sort2(E, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Q2c, Q2s))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))
print("merge_sort_threeway:")
print("time =", timeit.timeit("merge_sort_threeway(F, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(M1c, M1s))
print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))