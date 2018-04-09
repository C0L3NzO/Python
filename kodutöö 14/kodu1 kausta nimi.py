from os import listdir
from os.path import isdir, join

def f(kausta_nimi):
    
    for nimi in listdir(kausta_nimi):
        täisnimi = join(kausta_nimi, nimi) # võiks ka teha: täisnimi = kausta_nimi + "/" + nimi
        
        print(kausta_nimi, nimi)
        
        if isdir(täisnimi):
            try:
                f(täisnimi)
            except:
                # ilmselt ei õnnestunud kausta avada, kuna polnud õigusi vms.
                pass

