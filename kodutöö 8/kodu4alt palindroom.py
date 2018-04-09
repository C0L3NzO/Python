def on_palindroom(sisse):
    sõna=sisse.strip()
    y=1
    palindroom="True"
    if len(sõna)%2==0:
        while y<=len(sõna)//2:
            x=len(sõna)//2
            if sõna[x-1+y]!=sõna[x-y]:
                palindroom="False"
                break
            y+=1
        print(palindroom)
    else:
        while y<=len(sõna)//2:
            x=(len(sõna)//2)
            if sõna[x+y]!=sõna[x-y]:
                palindroom="False"
                break
            y+=1
        print(palindroom)
on_palindroom("jakovleva")