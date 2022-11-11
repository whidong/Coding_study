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
	while wordcounds[j+1] < wordcounds[j] and wordlenth[endindex[j]] + wordcounds[j+1] + 1 > W:
		check = None
		for k in range(len(endindex)-1, j, -1):
			if wordlenth[endindex[k]] + wordcounds[k+1] + 1 <= W:
				check = True
				wordcounds[k] -= wordlenth[endindex[k]] + 1
				wordcounds[k+1] += wordlenth[endindex[k]] + 1
				endindex[k] -= 1
				a = calculate_penalty(wordcounds, W)
				if a < penalty:
					penalty = a
		if check == None:
			break
	# 뒤의 값이 앞보다 작은데 넘길수 없는 상태일때 맨뒤에서부터 단어 하나씩 뒤로 넘겨주고 넘길수 있을때 까지 반복하도록 코드 작성
	# 만약 한칸씩 뒤로 넘겼는데도 넘길수 없다면 넘길수 있을때까지 반복하도록 코드 작성 
	while wordlenth[endindex[j]] + wordcounds[j+1] + 1 <= W and wordcounds[j+1] < wordcounds [j]:
		wordcounds[j] -= wordlenth[endindex[j]] + 1
		wordcounds[j+1] += wordlenth[endindex[j]] + 1
		endindex[j] -= 1
		a = calculate_penalty(wordcounds, W)
		if a < penalty:
			penalty = a
print(penalty)