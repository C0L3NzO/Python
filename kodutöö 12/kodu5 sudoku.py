import sys
failinimi=sys.argv[1]
f=open(failinimi)
fail=f.readlines()
f.close()
x=-1
okei="jah"
sudoku=[]
for i in fail:
    sudoku+=i.strip()
for i in sudoku:
    x+=1
    if i==" ":
        sudoku.pop(x)
def veerg(a):
    ajutine_hulk=set()
    ajutine_hulk.add(sudoku[0+a])
    ajutine_hulk.add(sudoku[9+a])
    ajutine_hulk.add(sudoku[18+a])
    ajutine_hulk.add(sudoku[27+a])
    ajutine_hulk.add(sudoku[36+a])
    ajutine_hulk.add(sudoku[45+a])
    ajutine_hulk.add(sudoku[54+a])
    ajutine_hulk.add(sudoku[63+a])
    ajutine_hulk.add(sudoku[72+a])
    if len(ajutine_hulk)!=9: return "vale"
    else: return "õige"

for i in range(9):
    if veerg(i)=="vale":
        okei="ei"
        
def rida(b):
    ajutine_hulk=set()
    ajutine_hulk.add(sudoku[0+b])
    ajutine_hulk.add(sudoku[1+b])
    ajutine_hulk.add(sudoku[2+b])
    ajutine_hulk.add(sudoku[3+b])
    ajutine_hulk.add(sudoku[4+b])
    ajutine_hulk.add(sudoku[5+b])
    ajutine_hulk.add(sudoku[6+b])
    ajutine_hulk.add(sudoku[7+b])
    ajutine_hulk.add(sudoku[8+b])
    if len(ajutine_hulk)!=9: return "vale"
    else: return "õige"

for i in range(9):
    if rida(i*9)=="vale":
        okei="ei"

def ruut(c):
    ajutine_hulk=set()
    ajutine_hulk.add(sudoku[0+c])
    ajutine_hulk.add(sudoku[1+c])
    ajutine_hulk.add(sudoku[2+c])
    ajutine_hulk.add(sudoku[9+c])
    ajutine_hulk.add(sudoku[10+c])
    ajutine_hulk.add(sudoku[11+c])
    ajutine_hulk.add(sudoku[18+c])
    ajutine_hulk.add(sudoku[19+c])
    ajutine_hulk.add(sudoku[20+c])
    if len(ajutine_hulk)!=9: return "vale"
    else: return "õige"

for i in range(3):
    for j in range(3):
        if ruut(i*3+j*27)=="vale":
            okei="ei"

if okei=="jah": print("OK")
else: print("Viga")

