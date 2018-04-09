x = int(input("Palun sisesta 2-st suurem täisarv: "))
print(x*"#" + "\n#" + int(x-2)*(int(x-2)*" " + "#\n#") + int(x-1)*"#")