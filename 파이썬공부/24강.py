dictionary = {
    "이름" : "구름",
    "종족" :"강아지"
}
print(dictionary.get("이름"))
print(dictionary["이름"])
if "나이" in dictionary:
    dictionary["나이"]
else:
    print("없는 키입니다.")