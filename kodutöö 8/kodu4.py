def on_palindroom(file):
    f=open(file)
    for line in f:
        rida=line.strip()
        y=1
        palindroom=""
        if len(rida)%2==0:
            while y<=len(rida)//2:
                x=len(rida)//2
                if rida[x-1+y]!=rida[x-y]:
                    palindroom="vale"
                    break
                y+=1
            if palindroom=="":
                print(rida)
        else:
            while y<=len(rida)//2:
                x=(len(rida)//2)
                if rida[x+y]!=rida[x-y]:
                    palindroom="vale"
                    break
                y+=1
            if palindroom=="":
                print(rida)
on_palindroom("")