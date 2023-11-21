def dfs(data, compare, v, n):
    if v == len(data):
        print(*compare)
        return
    for i in range(n):
        if data[i] not in compare:
            compare.append(data[i])
            dfs(data, compare, v+1, n)
            compare.pop()

n = int(input())
comp_list = []
list = [0] * n
for i in range(n):
    list[i] = i+1

dfs(list, comp_list, 0, n)