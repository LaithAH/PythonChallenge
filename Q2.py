L1= [10, 15, 20, 12, 25, 45, 18]
L2=[4, 5, 6, 3, 2, 9]
for i in L1:
    for x in L2:
        if i%x==0:
            print(x,'is a factor of',i)