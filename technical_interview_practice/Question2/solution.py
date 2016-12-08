
def question2(a):

    if not a:
        return None

    if len(a) == 1:
        return a

    n = len(a)
    w = 0
    res = ""
    tbl = [[0 for y in range(n)] for x in range(n)]

    for i in range(n):
        tbl[i][i] = 1

    for i in range(1, n):
        for k in range(n-i):
            x = k
            y = k+i

            if a[x] == a[y]:
                tbl[x][y] = 2 + tbl[x+1][y-1]

                if w < y-x+1:
                    w = x-y+1
                    res = a[x: y+1]

            else:
                tbl[x][y] = max(tbl[x-1][y], tbl[x][y-1])
    return res

print question2("bananas")
print question2("babad")
print question2("cbbd")
print question2("xyzqwer")