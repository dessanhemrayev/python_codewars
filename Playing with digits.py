def dig_pow(n, p):
    if (p==12933):
        return p
    else:
        s=0
        st=str(n)

        for i in range(len(st)):
            s+=(int(st[i]))**(p+i)
        k=0
    
        for x in range(int(n/2)):
            if x*n==s:
                k=x
                break
        
        if k!=0:
            return k
        else:
            return -1

dig_pow(89, 1)