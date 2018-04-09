def võitja(mäng):
    for i in mäng:
        if i[0]=="X" and i[1]=="X" and i[2]=="X":
            return("X")
        if i[0]=="O" and i[1]=="O" and i[2]=="O":
            return("O")

    if mäng[0][0]=="X" and mäng[1][0]=="X" and mäng[2][0]=="X" or mäng[0][1]=="X" and mäng[1][1]=="X" and mäng[2][1]=="X" or mäng[0][2]=="X" and mäng[1][2]=="X" and mäng[2][2]=="X":
        return("X")
    if mäng[0][0]=="O" and mäng[1][0]=="O" and mäng[2][0]=="O" or mäng[0][1]=="O" and mäng[1][1]=="O" and mäng[2][1]=="O" or mäng[0][2]=="O" and mäng[1][2]=="O" and mäng[2][2]=="O":
        return("O")
    if mäng[0][0]=="X" and mäng[1][1]=="X" and mäng[2][2]=="X" or mäng[0][2]=="X" and mäng[1][1]=="X" and mäng[2][0]=="X":
        return("X")
    if mäng[0][0]=="O" and mäng[1][1]=="O" and mäng[2][2]=="O" or mäng[0][2]=="O" and mäng[1][1]=="O" and mäng[2][0]=="O":
        return("O")
    return("?")

