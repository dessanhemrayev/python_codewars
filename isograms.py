def is_isogram(s):
    fl=True
    k=0
    if len(s)!=0:
        for x in s:
            if fl:
                k+=1
                i=0
                for i in range(k,len(s)):
                    if x==s[i]:
                        fl=False
                        break
            else:
                break
      
    return fl 


is_isogram("")