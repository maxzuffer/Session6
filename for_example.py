for i in range(1,10):
    print(i)

for i in range(1,10,3):
    print(i)


s = 0
for i in range(1,11):
    s += i
print(s)

s = 0
i = 1
while i <= 10:
    s += i
    i += 1 # This will break the loop
print(f"sum using while is also {s}")


