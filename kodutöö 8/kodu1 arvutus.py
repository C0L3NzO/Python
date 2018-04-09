def mediaan(list):
    järjest=sorted(list)
    if len(järjest)%2==0:
        x=len(järjest)//2
        med=(järjest[x-1]+järjest[x])/2
        return med
    else:
        x=(len(järjest)//2)
        med=järjest[x]
        return med
print(mediaan([2, 1, 3]))