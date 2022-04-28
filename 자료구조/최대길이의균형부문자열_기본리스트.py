def solve(A):
    a, b = 0, 0
    m, f=[], []
    g =[]
    for i in range(len(A)):
        if A[i] == '0':
            a += 1  
        else:
            b += 1
        if a-b not in m:
            m.append(a-b)
            g.append(i)
            if a-b == 0:
                f.append(0)
            else:
                f.append(i+1)
        else:
            p =m.index(a-b)
            del(g[p])
            g.insert(p, i)
    output = 0
    for i in range(len(m)):
        first = f[i]
        last = g[i]+1
        if last-first > output:
            output = last-first
    return output


A = input().strip()
print(solve(A))