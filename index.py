k = 1
for i in range(1,5+1):
    row = ""
    for j in range (1,i+1):
        row = row +str(k)+" "
        k=k+1
    print(row)