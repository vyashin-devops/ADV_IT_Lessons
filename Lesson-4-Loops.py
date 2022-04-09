# ============================================================
#   
#             Program by V.Yashin
#   
#   Version       Date            Info
#     1.0       09.04.2022    Initial Version
#
# ============================================================
num = 0

for x in range(0, 10):  # in range(0,10 -/+ 1) if you whant add or del last num in loop
    print(num)
    num += 1
    if num > 7:
        break
print("=====EOF=====")

rez = 0

while True:
    rez += 1
    if rez > 5:
        print("Resault is: " + str(rez) + "\n" + "Out of loop!")
        break
print("====EOWhile====")