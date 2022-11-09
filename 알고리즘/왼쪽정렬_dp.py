W = int(input())
words = input().split()
# code below
def calculate_penalty(A, W):
	penalty = 0
	for k in range(len(A)):
		penalty += (W - A[k])**3
	return penalty
	
wordlenth, wordcounds, endindex = [], [], []
count, penalty, countlen  = 0, [], 0
for i in range(len(words)):
	wordlenth.append(len(words[i]))
	if countlen + 1 + len(words[i]) <= W:
		if countlen == 0:
			countlen += len(words[i])
		else:
			countlen += len(words[i]) + 1
	elif countlen + 1 + len(words[i]) > W:
		endindex.append(i-1)
		wordcounds.append(countlen)
		count += 1
		countlen = 0
		countlen += len(words[i])
	if i == len(words)-1:
		wordcounds.append(countlen)
		count += 1
		countlen = 0
penalty.append(calculate_penalty(wordcounds, W))
for j in range(len(endindex)-1,-1,-1):
	if wordlenth[endindex[j]] + wordcounds[j+1] + 1 <= W:
		wordcounds[j] -= wordlenth[endindex[j]] + 1
		wordcounds[j+1] += wordlenth[endindex[j]] + 1
		endindex[j] -= 1
		penalty.append(calculate_penalty(wordcounds, W))
print(min(penalty))