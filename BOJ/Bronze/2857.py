# 2857

cnt = 0
fbi = ""

for i in range(1, 6):
    name = input()
    if "FBI" in name:
        cnt += 1
        fbi += str(i) + " "

if cnt == 0:
    print("HE GOT AWAY!")
else:
    print(fbi.rstrip())