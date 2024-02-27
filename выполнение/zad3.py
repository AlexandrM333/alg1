f = open('18.txt')
a = []
for i in range(100000):
    n = f.readline()
    n = n.replace(',', '.')
    a += [float(n)]
s = set()
max_summa = -100000
for i in range(1, len(a)):
    if a[i] - a[i-1] > 10:
        s.add(a[i-1])
        s.add(a[i])
    else:
        max_summa = max(max_summa, sum(s))
        s = set()
print(int(max_summa))