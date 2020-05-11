arr = []
n=1
maximum_number = None
minimum_number = None
while n>0:
    x = input("Enter a number: ")
    try:
        x=int(x)
    except:
        if x == 'done':
            break
        print("Invalid input")
        continue
    arr.append(x)
maximum_number = max(arr)
minimum_number = min(arr)
print("Maximum is", maximum_number)
print("Minimum is", minimum_number)
