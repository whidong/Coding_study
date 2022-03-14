def flatten(data):
    for key in data:
        if type(key)==int:
            output.append(key)
        else:
            for keys in key:
                if type(keys)==int:
                    output.append(keys)
                else:
                    for keyss in keys:
                        if type(keyss)==int:
                            output.append(keyss)
    return output
    

output = []
example=[[1,2,3],[4,[5,6]],7,[8,9]]
print("원본", example)
print("변환",flatten(example))
