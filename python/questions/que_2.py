list = []

for i in range(0,5):
    list.append(int(input("Enter the NUmbers - ")))

print(list)


a = list[0]
list[0] = list[len(list)-1]
list[len(list)-1] = a

print(list)