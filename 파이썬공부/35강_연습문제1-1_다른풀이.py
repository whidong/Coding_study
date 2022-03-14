def flatten(data):
    output = []
    for key in data:
        if type(key)==list:
            output += flatten(key)
        else:
            output +=[key]
        
    return output
#재귀함수로 풀기
#     

example=[[1,2,3],[4,[5,6]],7,[8,9]]
print("원본", example)
print("변환",flatten(example))