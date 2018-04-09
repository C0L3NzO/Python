ssõnak={}
f=open("fail.txt")
temp=f.readline()
for i in f:
    temp=i.strip().split(": ")
    temp2=temp[1].split(", ")
    ssõnak[temp[0]]=temp2
print(ssõnak)
print(ssõnak["August"])
f.close()
def on_eellane(A, B, number):
    if number==0:
        return "False"
    else:
        for i in ssõnak[A]:
            try:
                on=on_eellane(i, B, number-1)
                if on=="True":
                    return "True"
                if i==B:
                    return "True"
            except:
                return "False"
print(on_eellane("Joosep", "Leeni", 2))