"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Divison should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""

def zero(*arg): #your code here
    if arg.__len__()==0:
        return 0
    else:
        k=0
        s=str(arg[0])
        for x in s:
            if x=='+':
               k+=int(s[1]) 
            elif x=='-':

                k-=int(s[1]) 
            elif x=='*':
                k*=int(s[1]) 
            elif x=='/':
                k//=int(s[1]) 
    return  k     
def one(*arg): #your code here
    if arg.__len__()==0:
        return 1
    else:
        k=1
        s=str(arg[0])
        for x in s:
            if x=='+':
               k+=int(s[1]) 
            elif x=='-':

                k-=int(s[1]) 
            elif x=='*':
                k*=int(s[1]) 
            elif x=='/':
                k//=int(s[1]) 
    return  k     
def two(*arg): #your code here
    if arg.__len__()==0:
        return 2
    else:
        k=2
        s=str(arg[0])
        for x in s:
            if x=='+':
               k+=int(s[1]) 
            elif x=='-':

                k-=int(s[1]) 
            elif x=='*':
                k*=int(s[1]) 
            elif x=='/':
                k//=int(s[1]) 
    return  k     
def three(*arg): #your code here
    if arg.__len__()==0:
            return 3
    else:
        k=3
        s=str(arg[0])
        for x in s:
            if x=='+':
               k+=int(s[1]) 
            elif x=='-':

                k-=int(s[1]) 
            elif x=='*':
                k*=int(s[1]) 
            elif x=='/':
                k//=int(s[1]) 
    return  k     
def four(*arg): #your code here
    if arg.__len__()==0:
            return 4
    else:
        k=4
        s=str(arg[0])
        for x in s:
            if x=='+':
               k+=int(s[1]) 
            elif x=='-':

                k-=int(s[1]) 
            elif x=='*':
                k*=int(s[1]) 
            elif x=='/':
                k//=int(s[1]) 
    return  k     
def five(*arg): #your code here
    if arg.__len__()==0:
            return 5
    else:
        k=5
        s=str(arg[0])
        for x in s:
            if x=='+':
               k+=int(s[1]) 
            elif x=='-':

                k-=int(s[1]) 
            elif x=='*':
                k*=int(s[1]) 
            elif x=='/':
                k//=int(s[1]) 
    return  k     
def six(*arg): #your code here
    if arg.__len__()==0:
            return 6
    else:
        k=6
        s=str(arg[0])
        for x in s:
            if x=='+':
               k+=int(s[1]) 
            elif x=='-':

                k-=int(s[1]) 
            elif x=='*':
                k*=int(s[1]) 
            elif x=='/':
                k//=int(s[1]) 
    return  k     
def seven(*arg): #your code here
    if arg.__len__()==0:
        return 7
    else:
        k=7
        s=str(arg[0])
        for x in s:
            if x=='+':
               k+=int(s[1]) 
            elif x=='-':

                k-=int(s[1]) 
            elif x=='*':
                k*=int(s[1]) 
            elif x=='/':
                k//=int(s[1]) 
    return  k       
def eight(*arg): #your code here
    if arg.__len__()==0:
            return 8
    else:
        k=8
        s=str(arg[0])
        for x in s:
            if x=='+':
               k+=int(s[1]) 
            elif x=='-':

                k-=int(s[1]) 
            elif x=='*':
                k*=int(s[1]) 
            elif x=='/':
                k//=int(s[1]) 
    return  k     
def nine(*arg): #your code here
    if arg.__len__()==0:
            return 9
    else:
        k=9
        s=str(arg[0])
        for x in s:
            if x=='+':
               k+=int(s[1]) 
            elif x=='-':

                k-=int(s[1]) 
            elif x=='*':
                k*=int(s[1]) 
            elif x=='/':
                k//=int(s[1]) 
    return  k     


def plus(x): #your code here
    return "+"+str(x)
def minus(x): #your code here
    return "-"+str(x)
def times(x): #your code here
    return "*"+str(x)
def divided_by(x): #your code here
    return '/'+str(x)


print(seven(plus(five())))
print(seven(times(five())))
print(six(divided_by(two())))
print(eight(minus(three())))

"""

def zero(arg=""):  return eval("0" + arg)
def one(arg=""):   return eval("1" + arg)
def two(arg=""):   return eval("2" + arg)
def three(arg=""): return eval("3" + arg)
def four(arg=""):  return eval("4" + arg)
def five(arg=""):  return eval("5" + arg)
def six(arg=""):   return eval("6" + arg)
def seven(arg=""): return eval("7" + arg)
def eight(arg=""): return eval("8" + arg)
def nine(arg=""):  return eval("9" + arg)

def plus(n):       return "+%s" % n
def minus(n):      return "-%s" % n
def times(n):      return "*%s" % n
def divided_by(n): return "/%s" % n
"""