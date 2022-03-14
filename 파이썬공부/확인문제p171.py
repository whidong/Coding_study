

pets =[
    {"name":"구름","age": 5},
    {"name":"초코","age": 3},
    {"name":"아지","age": 3},
    {"name":"호랑이","age": 1}
]
print('#우리 동네 애완 동물들')
for key in pets:
    print("{} {}살".format(key["name"], key["age"]))