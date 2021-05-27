

#function to calculate distance
def compute_dis(x1,y1,x2,y2):
    #initial value of distance for each case
    distance = 0
    #fromula to calculate distance
    distance = ((x2-x1)**2) + ((y2-y1)**2)**0.5
    dis_decimal = "{:.2f}".format(distance)
    print(dis_decimal,"\n")
#T no. of testes
test = int(input("Enter the number of tests you want to run"))


for i in range(test):
    print("Enter the positon of point 'A' in terms of (x,y): ")
    x1 = int(input())
    y1 = int(input())
    print("Enter the positon of point 'B' in terms of (x,y): ")
    x2 = int(input())
    y2 = int(input())
    compute_dis(x1,y1,x2,y2)
