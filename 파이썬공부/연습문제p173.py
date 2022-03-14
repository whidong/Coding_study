character ={
    "name":"기사",
    "level":"12",
    "item":{
        "sward":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}
for key in character:
    if type(character[key]) is str:
        print("{} : {}".format(key, character[key]))
    elif type(character[key]) is dict:
        for keys in character[key]:
            print("{}:{}".format(keys, character[key][keys]))
    elif type(character[key]) is list:
        for keyss in character[key]:
            print(key,":",keyss)