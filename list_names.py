
def namelist(names):
    length_of_list=names.__len__()
    a=''
    if length_of_list!=0:
        for x in range(length_of_list):
            if length_of_list==1:
                a+=names[x]['name']
           
            elif  x==length_of_list-1:
                a+='& '+ names[x]['name']
            elif  x==length_of_list-2:
                a+=names[x]['name']+' '
            else:
                a+=names[x]['name']+', '
    return a


"""def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']
"""
print ("test 1")
print(namelist([{'name': 'Bart'}]))
print ("test 2")
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))