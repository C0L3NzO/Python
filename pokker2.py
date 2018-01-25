def käsi(a, b, c, d, e):

    def mastid(m):
        try:
            if m[2]=='h':
                return 'h'
            elif m[2]=='d':
                return 'd'
            elif m[2]=='c':
                return 'c'
            elif m[2]=='s':
                return 's'
        except:
            if m[1]=='h':
                return 'h'
            elif m[1]=='d':
                return 'd'
            elif m[1]=='c': 
                return 'c'
            elif m[1]=='s':
                return 's'

    def numbrid(n):
        try:
            return (int(n[0]+n[1]))
        except:
            try:
                if int(n[0])>=2 or int(n[0])<=9:
                    return int(n[0])
            except:
                if n[0]=='J':
                    return 11
                elif n[0]=='Q':
                    return 12
                elif n[0]=='K':
                    return 13
                elif n[0]=='A':
                    return 14

    k1n=numbrid(a)
    k2n=numbrid(b)
    k3n=numbrid(c)
    k4n=numbrid(d)
    k5n=numbrid(e)
    
    k1m=mastid(a)
    k2m=mastid(b)
    k3m=mastid(c)
    k4m=mastid(d)
    k5m=mastid(e)

        
    if k1m==k2m and k2m==k3m and k3m==k4m and k4m==k5m:
        mast="jah"
    else:
        mast="ei"
    
    if k5n==k4n+1 and k4n==k3n+1 and k3n==k2n+1 and k2n==k1n+1 or k2n==k1n+1 and k3n==k2n+1 and k4n==k3n+1 and k5n==14:
        rida="jah"
    else:
        rida="ei"
        
        
    if mast=="jah" and rida=="jah" and k1n==10:
        return("Kuninglik mastirida")

    if mast=="jah" and rida=="jah":
        return("Mastirida")
    
    if mast=="jah" and rida=="ei":
        return("Mast")

    if mast=="ei" and rida=="jah":
        return("Rida")

    if k1n == k2n == k3n == k4n or k2n == k3n == k4n == k5n:
        return("Nelik")

    
    if k1n==k2n==k3n and k4n==k5n or k1n==k2n and k3n==k4n==k5n:
        return("Maja")
    
    
    if k1n==k2n==k3n or k2n==k3n==k4n or k3n==k4n==k5n:
       return("Kolmik")
    
    
    if k1n==k2n and k3n==k4n or k1n==k2n and k4n == k5n or k2n == k3n and k4n == k5n:
        return("Kaks paari")

    
    if k1n == k2n or k2n == k3n or k3n == k4n or k4n == k5n:
        return("Üks paar")
    else:
        return("Kõrge kaart")

print(käsi("Jh", "3h", "7h", "1h", "Kh"))