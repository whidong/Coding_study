
def countrot(A):
	count, i , z = 0, 0, len(A)-1
	m = A[0]
	while True:
		if z == i and m < A[i]:
			return len(A)-1
			break
		elif len(A)%2 == 0 and i == len(A)/2-1 and A[i] >= A[z]:
			return len(A)-1
			break
		if A[i] >= A[z]:
			count += 1
		else:
			if m > A[i]:
				count += 2
				return count
				break
			elif m < A[i] or m < A[z]:
				return count
				break
		m = A[i]
		i += 1
		z -= 1
A = list(map(int,input().split()))
print(countrot(A))