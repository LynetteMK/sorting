def values(a):
    even = []
    odd = []
    chars = []
    for n in a:
        if isinstance(n, int):
            if n % 2 == 0:
                even.append(n)
    for x in range(0,len(a)):
        if isinstance(a[x], int):
            if int(a[x]) % 2 != 0:
                odd.append(a[x])
    for z in a:
        if isinstance(z, str):
            chars.append(z)
    dic = {}
    dic["even"] = even
    dic["odd"] = odd
    dic["chars"] = chars
    return dic