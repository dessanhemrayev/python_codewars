def hanoi(n,i,k):
    if(n==1):
        print("Move disk 1 from pin",i ,"to",k, sep=" ")
    else:
        tmp=6-i-k
        hanoi(n-1,i,tmp)
        print("Move disk",n,"from pin",i,"to",k, sep=" ")
        hanoi(n-1,tmp,k)

hanoi(3,1,2)
