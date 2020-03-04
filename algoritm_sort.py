"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""

def move_zeros(array):
    kl=''
    for x in array:
        if x==0:
            kl=str(x)
            if kl!="False":
            
                k=array.index(0)
                del array[k]
                array.append(x)
            
    #return array     
    print(array)

    
move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])

move_zeros(["a",False,0,"b",None,"c","d",0,1,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
move_zeros([1,2,0,1,0,1,0,3,0,1])
move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])
move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9])