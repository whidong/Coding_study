import time, random

def compute_e_ver1(n):
	result = 0
	for i in range(0, n+1):
		save = 1
		for k in range(1, n+1):
			if k < i+1:
				save = save*k
		result = result + (1/save)
	return result
	
def compute_e_ver2(n):
	result = 0
	save = 1
	for i in range(0,n+1):
		if i > 0:
			result = result + (1/(i*save))
			save = save*i
		else:
			result += 1
	return result

n = int(input())

before_1 = time.process_time()
print(compute_e_ver1(n))
after_1 = time.process_time()
print(after_1 - before_1)
before_2 = time.process_time()
print(compute_e_ver2(n))
after_2 = time.process_time()
print(after_2 - before_2)
