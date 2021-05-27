##n = 9429
##def func(n):
##    s = 0
##    rem = 0
##    rem = n % 10
##    n = n //10
##    if n == 0:
##        return n
##    else:
##        s = rem + func(n)
##        return s
##
##a = func(n)
##if a%10==a:
##    print(a)
##    
##else:
##    print(func(a))
def func(n):
    while (n>10):
        n = n % 10 + n //10
    return n
print(func(493193))
