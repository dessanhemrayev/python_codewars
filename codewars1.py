def unique_in_order(iterable):
    a=[]
    if len(iterable)!=0:
        a.append(iterable[0])
        for x in range(1,len(iterable)):
            if iterable[x]==iterable[x-1]:
                continue
            else:
                a.append(iterable[x])
        
    return a


unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD') 
unique_in_order([1,2,2,3,3]) 