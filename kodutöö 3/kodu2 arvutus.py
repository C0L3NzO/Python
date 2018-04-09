palk_e=int(input("Mis on ema palk? "))
palk_i=int(input("Mis on isa palk? "))
lapsi=int(input("Mitu alaealist last on peres? "))
if palk_e > 170:
    arv_e=palk_e-170
    ema=arv_e*0.79+170
else:
    ema=palk_e
    
if palk_i > 170:
    arv_i=palk_i-170
    isa=arv_i*0.79+170
else:
    isa=palk_i

palk_l=lapsi*50
sissetulek=round(ema+isa+palk_l, 2)
print("Pere sissetulek on "+ str(sissetulek) +" eurot.")