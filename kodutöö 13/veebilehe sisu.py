from urllib.request import urlopen
 
f = urlopen("http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_Dinov_020108_HeightsWeights")
lehekülje_sisu = f.read().decode("UTF-8")
f.close()
print(lehekülje_sisu)

for i in lehekülje_sisu:
    if i=="<tr>":
        info=rida
        print(rida)

