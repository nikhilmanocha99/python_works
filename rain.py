'''#map
li = [1,2,3,4,5,6,7,8,9,10]
def func(x):
    return x**x
newlist = []
for x in li:
    newlist.append(func(x)

print(newlist)

#print(list(map(func, li))
print([x.split(',') for x in li]
'''
'''def func(x):
    return x+7

fun = lambda x: ' '.join(x)
print(fun(['to', 'the', 'sweet', 'desire', 'welcome']))
'''
#import collections
#from collections import Counter, namedtuple, deque

'''c = Counter('gallad')
print(list(c.elements()))
print(c['l'])
print(c.most_common(3))
c = Counter([1,2,3,4,5])
print(c)

point = namedtuple('point', 'z')

newp = point(1)
print(newp)
'''
#a = deque('hello')
#print(a)
'''int = 5
while int<=1:
    print(int)
    int = int-1
'''







































##def digital_root(n):
##    # ...
##    a = n
##    while (a//10 != 0):
##        
##        rem = n % 10
##        n = n//10
##        if n==0:
##            return n
##        else:
##            a = rem+digital_root(n)
##            return a
##    
##number= 16
##print(digital_root(number))

from pymysql import connect
connection = connect(host='localhost', user='root', password='1234qwerty')

def display():
    while True:
        print("Press 1. To create table \n Press 2. To display table \n Press 3. To edit table\n press 4. To delete the table \n press 5. to search in table \n press 6. to exit")
        ch = int(input())
        if(ch==1):
            create()
        elif(ch==2):
            display()
        elif(ch==3):
            edit()
        elif(ch==4):
            delete()
        elif(ch==5):
            search()
            
