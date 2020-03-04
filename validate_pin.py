def validate_pin(pin):
    a="0123456789"    
    k=len(pin)
    l=0
    kl=0
    if k==6 or k==4:
        while(k>l):
            for i in range(len(a)):
                if a[i]==pin[l]:
                    kl+=1  
                    break 
            l+=1

 if kl==6 or kl==4:
        return True
    else:
        return False


validate_pin("1234")
validate_pin("098765")
validate_pin("-1.234")