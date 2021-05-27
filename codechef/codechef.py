#T represents the no. of test cases
T = int(input("Enter the no. of cases you want to run"))
# list to store the integers
list = []
for x in range(T):
    num = int(input("Enter the no: "))
    list.append(num)
#Satisfy the conditions and run the programm
for n in list:
    print("\n")
    for i in range(n):
       if i!=0 :
          if i%2==0:
            print(i*2, end=" ")
          else:
            print(i**2, end=" ")
       else:
          print(i+3, end=" ")
       
