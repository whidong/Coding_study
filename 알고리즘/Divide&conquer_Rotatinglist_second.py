def countrot(A):
	if len(A) == 1:
		return 0
	if A[0] < A[-1]:
		return 0

	else:
		return secondstep(A, 0, len(A)-1, len(A)//2-1)


def secondstep(A, s, e, m):
	a, b, c = A[m-1], A[m], A[m+1]
	if a > b:
		return len(A) - m
	elif c < b:
		return len(A) - m -1
	elif A[m] > A[s]:
		return secondstep(A, m, e, (m+e)//2)
	elif A[m] < A[e]:
		return secondstep(A, s, m, (s+m)//2)


A = list(map(int,input().split()))
print(countrot(A))