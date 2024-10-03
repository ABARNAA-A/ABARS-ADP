m=[215,567,341,678]
for i in m:
    s=0
    for j in str(i):
        s=s+int(j)
    if s==8:
        print(i)
