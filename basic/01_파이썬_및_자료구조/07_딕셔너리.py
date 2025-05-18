# 딕셔너리
# 1. get
users = {"kyle": 20, "alex": 30, "jun": 40}
print(users["kyle"])  # 20
print(users.get("kyle"))  # 20

print(users.get("kitty"))  # None
print(users.get("kitty", 0))  # 0
# print(users["kitty"])  # KeyError

# 2. keys, values, items
users = {"kyle": 20, "alex": 30, "jun": 40}

for key in users.keys():
    print(key)

for key in users:
    print(key)

for value in users.values():
    print(value)


for key, value in users.items():
    print(f"{key} : {value}")

for key in users:
    print(f"{key} : {users[key]}")
