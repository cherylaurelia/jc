arr = [0,2,12,45,78,90]
upper = len(arr) - 1
lower = 0
middle = int((upper+lower) / 2)

searchelement = int(input("Enter search element: "))

found = False

while not found:
    if arr[middle] == searchelement:
        print(f"Found at index {middle}")
        found = True
    elif searchelement > arr[middle]:
        lower = middle + 1
        middle = int((upper+lower)/ 2)
    elif searchelement < arr[middle]:
        upper = middle - 1
        middle = int((upper+lower) / 2)

if found:
    print("element found")
