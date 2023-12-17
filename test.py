def DragonSlayer(A,B,C,D):
    count=1
    while(A or C >=0):
        if(count%2!=0):
            A=A-D
            count=count+1
            if(A<=0):
                print("Natsu's Win")
        if(count%2==0):
            C=C-B
            count=count+1
            if(C<=0):
                print("Dragon's Win")

DragonSlayer(8,2,5,3)