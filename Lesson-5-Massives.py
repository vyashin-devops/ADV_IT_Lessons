# ============================================================
#   
#             Program by V.Yashin
#   
#   Version       Date            Info
#     1.0       09.04.2022    Initial Version
#
# ============================================================

names = ['Slava', 'Vasya', 'Petya', 'Kolya']
for i in range(0,len(names)):
    print("Hello, " + names[i])

for i in range(0, len(names)):
    for j in range(len(names)):
        print(names[i][j])
names[1] = 'Dinara'
names.append('Misha')
print(names)

names.insert(2,'Naddy')
print(names)
print(len(names))
del names[3]
del names[-2]
print(names)
names.remove('Misha')
print(names)
deleted_name = names.pop()
print("Deleted name is " + deleted_name)
print(names)
names.reverse()
print(names)