a, p = map(str, input().split())
p = int(p)

D = ['temp', a]
i = 1
check = True
insert_value = 0
while check:
    for j in D[i]:
        insert_value += int(j)**p
    for k in range(1, len(D)):
        if D[k] == str(insert_value):
            result = k - 1
            check = False
            break
    D.append(str(insert_value))
    insert_value = 0
    i += 1
print(result)
    