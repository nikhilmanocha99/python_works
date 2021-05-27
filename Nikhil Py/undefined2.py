'''
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code SLICE_PY
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            SLICE_PY.py
*  Created:             04/10/2020
*  Last Modified:       04/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
'''
 
# Main function
if __name__ == '__main__':
    
   
    try:
         # Take the T (test_cases) input
        test_cases = int(input())
        # Write your code from here
        L = []
        length = int(input())
        #loop to iterate the programe as per the no. of tests
        for x in range(test_cases):
    
            #Enter elemnts in list
    
            L = list(int(num) for num in input().split())
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
            for j in range(3,8):
                compute+=L[j]

            print(compute)
    except:
        pass
    
