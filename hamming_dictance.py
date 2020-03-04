def dictance(str1,str2):
    k=0
    l1=len(str1)
    l2=len(str2)
    if l1>l2:
        k=l1-l2
    else:
        k=l2-l1
    l=0
    while(l1>l):
        if str1[l]!=str2[l]:
            k+=1
        l+=1
    return k

print(dictance('01101', '11001'))