import functools



def generate_AP(a1, d, n):

    for i in range(0, n):
        print(a1, end=' ')
        AP_series.append(a1)
        a1+=d
    return AP_series

#test cases
T = int(input("Enter the number of times you want to test the programe"))
for i in range(T):
    AP_series = []
    print("Enter the first term of A.P, diiference between the terms and the number of terms you want in a series respectively: ")
    a1=int(input())
    d=int(input())
    n=int(input())
    generate_AP(a1, d, n)
    print("\n")
    #creatin and using lambda and map function
    sqr_AP = lambda x: x*x
    sqr_AP_series = map(sqr_AP, AP_series)
    sqr_series=list(sqr_AP_series)
    print(sqr_series)
    #lambda function to find the sum of AP
    sum_func = lambda a,b : a+b
    sum_AP = functools.reduce(sum_func, sqr_series)
    print(sum_AP)









