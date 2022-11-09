W = int(input())
words = input().split()
# code below
def calculate_penalty(A, W):
	penalty = 0
	for k in range(len(A)):
		penalty += (W - A[k])**3
	return penalty
	
wordlenth, wordcounds, endindex = [], [], []
count, allen, countlen  = 0, 0, 0
for i in range(len(words)):
	wordlenth.append(len(words[i]))
	if countlen + 1 + len(words[i]) <= W:
		if countlen == 0:
			allen += len(words[i])
			countlen += len(words[i])
		else:
			allen += len(words[i])
			countlen += len(words[i]) + 1
	elif countlen + 1 + len(words[i]) > W:
		endindex.append(i-1)
		wordcounds.append(countlen)
		count += 1
		countlen = 0
		allen += len(words[i])
		countlen += len(words[i])
	if i == len(words)-1:
		wordcounds.append(countlen)
		count += 1
		countlen = 0
penalty = calculate_penalty(wordcounds, W)
for j in range(len(endindex)-1,-1,-1):
	while wordlenth[endindex[j]] + wordcounds[j+1] + 1 <= W and wordcounds[j+1] < wordcounds [j]:
		wordcounds[j] -= wordlenth[endindex[j]] + 1
		wordcounds[j+1] += wordlenth[endindex[j]] + 1
		endindex[j] -= 1
		a = calculate_penalty(wordcounds, W)
		if a < penalty:
			penalty = a
print(penalty)