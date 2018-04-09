
def abs_list(list):
    uus_list=[]
    for i in list:
        uus_list+=[abs(i)]
    return uus_list
print(abs_list([11,-2,1,2,-3,-4]))