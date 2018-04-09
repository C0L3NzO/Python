from random import randint
def minu_shuffle(list):
    segi_list=[]
    while list!=[]:
        x=randint(1,len(list))
        segi_list.append(list[x-1])
        list.pop(x-1)
    return(segi_list)
print(minu_shuffle([1,2,3,4,5,6,7]))