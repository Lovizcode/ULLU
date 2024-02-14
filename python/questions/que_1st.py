list = []

for i in range(0,5):
    list.append(int(input("enter number - ")))
    un = int(input("Enter a Number to Check - "))
    if(un==list[i]):
        print("This Number is Already in List")
    else:
        print("This Number is not in the list ")