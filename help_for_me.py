

p=''
op=''
df=0
print(kl)
for j in range(kl.__len__()):
    df=0
    for l  in range(len(alfawit)):
        for k  in range(len(alfawit)):
            if ((l+k)%32)==kl[j]:
                df+=1
               # print (df,alfawit[l],alfawit[k],key[j], sep=" ")
                p+=alfawit[l]
                op+=alfawit[k]
jk=0
ol=''
try:
    for g in range(len(p)):
        ol=''
        if len(p)-33:

            for t in range(g,len(p),33):
                ol+=op[t]
                jk+=1
                if jk==6:
                    print(ol)
                    jk=0
                    
except IndexError:
    ol+=''

