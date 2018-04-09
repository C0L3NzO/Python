import datetime
now = datetime.datetime.now()
kuupaev = (str(now)[8] + str(now)[9])

x = 0
f = open("t.txt")
for i in f:
    x += 1
    if x == int(kuupaev):
        print(i)