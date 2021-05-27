
#No. of tests(T)
T = int(input())


#loop to iterate the programe as per the no. of tests
for x in range(T):
    length = int(input())
    
    #Enter elemnts in list
    L = []
    
    L = list(map(int,input().split()))
    #real list
    print(L)
    #list in reverse order
    print(L[::-1])
    #Adding 3 to the element if the element is on third place
    for i in range(1,length):
        if (i%3 == 0):
            a = L[i] + 3
            print(a, end=" ")
        else:
            continue
    print()
    #Subtracting 7 from an element if element is on 7th place
    for i in range(1,length):
        if (i%5 == 0):
            b = L[i] - 7
            print(b, end=" ")
    print()
    compute=0
    for j in range(3,length):
        compute+=L[j]

    print(compute)
            
