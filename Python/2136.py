#pandas import doesnt work in beecrowd.... WHY?
def drop_duplicates(names):
    no_duplicated = []
    for name in names:
        if(name not in no_duplicated):
            no_duplicated.append(name)
    return no_duplicated

yes = []
no = []
while True:
    data = input().split()
    if (data[0] == 'FIM'):
        break
    elif(data[1] == 'YES' and data[1] not in yes):
        yes.append(data[0])
    elif(data[1] == 'NO' and data[1] not in no):
        no.append(data[0])
j = 0
name = ''

for i in range(len(yes)):
    if(len(yes[i]) > j):
        name = yes[i]
        j = len(yes[i])
yes.sort()
no.sort()
yes = drop_duplicates(yes)
no = drop_duplicates(no)

for i in range(len(yes)):
    print(yes[i])
for i in range(len(no)):
    print(no[i])

print()
print('Amigo do Habay:')
print(name)