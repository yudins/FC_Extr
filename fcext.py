l = []
lout = []
lfull = [i for i in range(0,256)]
lfree = []

with open('in.csv', 'r') as f:
    l = [line[8:10].strip() for line in f]
print('Cards total: ', len(l))

for i in l:
    if int(i,16) not in lout:
        lout.append(int(i,16))
lout.sort()

for i in lfull:
    if int(i) not in lout:
        lfree.append(int(i))

with open('out_used.csv', 'w') as foutused:
    for i in lout:
        foutused.write(str(i))
        foutused.write('\n')

with open('out_free.csv', 'w') as foutfree:
    for i in lfree:
        foutfree.write(str(i))
        foutfree.write('\n')

print('FC\'s used: ',lout)
print('FC\'s free: ',lfree)
print('Done')
#print(len(lout), len(lfree)) 'Проверка: сумма должна быть равна 256