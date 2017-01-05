def mul(n):
    if n % 7 == 0:
        return "abc"
    if n % 13 == 0:
        return "xyz"
    if (n % 13 == 0 and n % 7 == 0):
        return "a-z"
    else:
        return n



for i in range(30,301,1):
    out_ = mul(i)
    print(out_)
