a = str(input())
b = len(a)
p = int(input())-1
c = []
v = []
mm = []

for i in range(p+1):
    gh = str(input())
    v.append(gh)

for i in range(b):
    c.append(0)
for i in range(1, p):
    c.append(i)
for i in range(b*2):
    c.append(p)
for i in range(1, p):
    c.append(p-i)
for i in range(b):
    c.append(0)

g = (b*4) + ((p-1)*2)

for i in range(g-b+1):
    t = c[i:i+b]
    l = ''
    for j in range(len(t)):
        l = l + '-' + str(t[j]) + a[j]
    for n in range(0, p+1):
        while (l.find(('-' + str(p-n))) != -1):
            oo = str('-' + str(p-n))
            l = l.replace(oo, v[n])
    mm.append(l)
    
print('---===>>> LEFT <<<===---')
for i in mm:
    print('  - \'' + i +'\'')
mm = mm[::-1]
print('---===>>> RIGHT <<<===---')
for i in mm:
    print('  - \'' + i +'\'') 
