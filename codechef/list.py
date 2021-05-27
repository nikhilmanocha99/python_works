n = int(input("Enter the size of the list "))
print("\n")
numList = list(int(num) for num in input("Enter the list numbers separated by space ").strip().split())[:n]
print("User List: ", numList)
