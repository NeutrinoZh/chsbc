import time

a = '''
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
'''

b =  '''
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
    5409890684902869042869042869084209684209869023859742986702476848734879847598427598427589274
    6478679483679483678943769843768943769824705928409682409674982768947628946987298579248759322
'''

def school_method(x, y):
    n = len(x)
    res = [0]*(2*n)

    for i in range(n):
        for j in range(n):
            if res[i + j] == None:
                res[i + j] = 0
            res[i + j] += x[i] * y[j]

    while True:
        one = True
        for i in range(1, len(res)):
            num = res[i] // 10
            res[i - 1] += num
            res[i] %= 10

            one = one and (num == 0)
        
        if one:
            break

    new_res = res.copy()


    return new_res

def karatsuba(x, y):
    n = len(x)

    if n <= 128:
        return school_method(x, y)

    res = [0]*(2*n)
    k = n // 2

    xr = [x[i] for i in range(0, k)]
    xl = [x[i] for i in range(k, len(x))]
    yr = [y[i] for i in range(0, k)]
    yl = [y[i] for i in range(k, len(y))]

    p1 = karatsuba(xl, yl)
    p2 = karatsuba(xr, yr)

    xlr = [0]*k
    ylr = [0]*k

    for i in range(k):
        xlr[i] = xl[i] + xr[i]
        ylr[i] = yl[i] + yr[i]
    
    p3 = karatsuba(xlr, ylr)

    for i in range(n):
        p3[i] -= p2[i] + p1[i]

    for i in range(n):
        res[i] = p2[i]

    for i in range(n, 2 * n):
        res[i] = p1[i - n]

    for i in range(k, n + k):
        res[i] += p3[i - k]

    return res

def finalize(res):
    while True:
        one = True
        for i in range(1, len(res)):
            num = res[i] // 10
            res[i - 1] += num
            res[i] %= 10

            one = one and (num == 0)
        
        if one:
            break
    return res

def foo(x, y):
    x = [int(i) for i in x if i.isdigit()]
    y = [int(i) for i in y if i.isdigit()]

    n = max(len(x), len(y))

    while n & (n - 1):
        n += 1

    def extend(v):
        v = v[::-1]
        v.extend([0 for i in range((n - len(v)))])
        v = v[::-1]
        return v

    x = extend(x)
    y = extend(y)

    res = finalize(karatsuba(x, y))
    res.pop()
    new_res = res.copy()
    for i in res:
        if i == 0: new_res.remove(0)
        else: break
    return new_res

t = time.process_time()
res = foo(a, b)
new_res = [str(i) for i in res]
print(''.join(new_res))

print('time:', time.process_time() - t)