arr = [2, 4, 6, 8, 10]
print(arr)

search = int(input("Enter element to search : "))

found = False

for i in range(len(arr)):
    if arr[i] == search:
        print("Element found at index :", i)
        found = True
        break

if not found:
    print("Element not found")
